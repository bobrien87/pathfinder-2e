import os
import json
import re
import sys
import subprocess

# Define source directories and target directory
PF2E_DIR = "/Users/personal/.gemini/antigravity/pf2e"
PF2E_PACKS_DIR = os.path.join(PF2E_DIR, "packs/pf2e")
OUTPUT_DIR = "/Users/personal/Obsidian Vaults/Pathfinder 2e/8. System/Creatures"
LANG_FILE = os.path.join(PF2E_DIR, "static/lang/en.json")

LOCALIZATION_DICT = {}

def sync_repository():
    if not os.path.exists(PF2E_DIR):
        print(f"Cloning Foundry PF2e repository to {PF2E_DIR}...")
        os.makedirs(os.path.dirname(PF2E_DIR), exist_ok=True)
        try:
            subprocess.run([
                "git", "clone", "--depth", "1",
                "https://github.com/foundryvtt/pf2e.git", PF2E_DIR
            ], check=True)
            print("Cloned successfully.")
        except Exception as e:
            print(f"Error cloning repository: {e}")
            sys.exit(1)
    else:
        print(f"Updating Foundry PF2e repository in {PF2E_DIR}...")
        try:
            subprocess.run(["git", "pull"], cwd=PF2E_DIR, check=True)
            print("Updated successfully.")
        except Exception as e:
            print(f"Warning: could not pull remote changes (offline?): {e}")

def load_localization():
    global LOCALIZATION_DICT
    try:
        with open(LANG_FILE, "r") as fh:
            LOCALIZATION_DICT = json.load(fh)
        print("Successfully loaded localization database.")
    except Exception as e:
        LOCALIZATION_DICT = {}
        print(f"Warning: could not load localization file: {e}")

SIZE_MAP = {
    "tiny": "Tiny",
    "sm": "Small",
    "med": "Medium",
    "lg": "Large",
    "huge": "Huge",
    "grg": "Gargantuan"
}

def format_mod(val):
    try:
        val = int(val)
        return f"+{val}" if val >= 0 else str(val)
    except:
        return str(val)

def ordinal(n):
    if 11 <= n % 100 <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"

def should_exclude_ability(name):
    name_lower = name.lower().strip()
    generic_rules = [
        "darkvision",
        "greater darkvision",
        "low-light vision",
        "scent",
        "tremorsense",
        "lifesense",
        "wavesense",
        "truesight",
        "void healing"
    ]
    for rule in generic_rules:
        if name_lower == rule:
            return True
        if name_lower.startswith(rule + " "):
            return True
        if name_lower.startswith(rule + "(") or name_lower.startswith(rule + " ("):
            return True
    return False

def get_localization(key):
    parts = key.split(".")
    curr = LOCALIZATION_DICT
    for p in parts:
        if isinstance(curr, dict) and p in curr:
            curr = curr[p]
        else:
            return f"[{key}]"
    return curr if isinstance(curr, str) else f"[{key}]"

def expand_localization(html):
    def replace_localize(m):
        key = m.group(1)
        val = get_localization(key)
        return val
    return re.sub(r"@Localize\[([^\]]+)\]", replace_localize, html)

def format_effect_title(name):
    name_clean = name.replace("-", " ").strip()
    if name_clean.lower().startswith("effect:"):
        name_clean = name_clean[7:].strip()
    elif name_clean.lower().startswith("effect "):
        name_clean = name_clean[7:].strip()
    if not name_clean:
        return "Effect"
    if name_clean.islower():
        name_clean = name_clean.title()
    return f"Effect: {name_clean}"

def clean_html(html):
    if not html:
        return ""
    
    # Expand localization keys first
    html = expand_localization(html)
    
    # Replace action glyphs
    html = re.sub(r"<(span|i) class=\"[^\"]*(action-glyph|pf2-icon)[^\"]*\">([0-9rfF])</\1>", lambda m: f"`pf2:{m.group(3).lower()}`", html)
    # Replace action words
    html = html.replace("[one-action]", "`pf2:1`").replace("[two-actions]", "`pf2:2`").replace("[three-actions]", "`pf2:3`").replace("[reaction]", "`pf2:r`").replace("[free-action]", "`pf2:0`")
    
    # Replace common HTML tags
    html = re.sub(r"<p\b[^>]*>", "", html)
    html = html.replace("</p>", "\n\n")
    html = re.sub(r"<br\s*/?>", "\n", html)
    html = re.sub(r"<strong>(.*?)</strong>", r"**\1**", html)
    html = re.sub(r"<b>(.*?)</b>", r"**\1**", html)
    html = re.sub(r"<em>(.*?)</em>", r"*\1*", html)
    html = re.sub(r"<i>(.*?)</i>", r"*\1*", html)
    html = re.sub(r"<ul\b[^>]*>", "", html)
    html = html.replace("</ul>", "\n")
    html = html.replace("<li>", "- ")
    html = html.replace("</li>", "\n")
    
    # Replace Check tags: @Check[fortitude|dc:34] save -> DC 34 [[Fortitude]] save
    def replace_check(m):
        c_type = m.group(1).replace("-", " ")
        dc_val = m.group(2)
        c_type = c_type.capitalize()
        
        if c_type == "Flat":
            check_name = "flat check"
        elif c_type in ["Fortitude", "Reflex", "Will"]:
            check_name = f"[[{c_type}]] save"
        elif c_type in ["Athletics", "Acrobatics", "Stealth", "Perception", "Arcana", "Crafting", "Deception", "Diplomacy", "Intimidation", "Medicine", "Nature", "Occultism", "Religion", "Society", "Survival", "Thievery"]:
            check_name = f"[[{c_type}]] check"
        else:
            check_name = f"{c_type} check"
            
        if dc_val:
            return f"DC {dc_val} {check_name}"
        return check_name

    html = re.sub(r"@Check\[([^\]\|]+)(?:\|dc:(\d+))?[^\]]*\](?:\s+(saves?|checks?))?", replace_check, html)
    
    # Replace Damage tags: @Damage[4d6[fire]] -> 4d6 fire or @Damage[250[healing]]{250 Hit Points} -> 250 Hit Points
    def replace_damage(m):
        formula = m.group(1)
        display_text = m.group(2)
        if display_text:
            return display_text
        return formula.replace("[", " ").replace("]", "").strip()

    html = re.sub(r"@Damage\[([a-zA-Z0-9\+\-\s*d]+(?:\[[^\]]+\])?)\](?:\{([^\}]+)\})?", replace_damage, html)
    
    # Clean up double bracket chat buttons: [[/gmr ...]]{text} -> text
    html = re.sub(r"\[\[/(.*?)\]\]\{(.*?)\}", r"\2", html)
    html = re.sub(r"\[\[/(.*?)\]\]", r"`\1`", html)
    
    # Replace UUID links with text
    def replace_uuid(m):
        path = m.group(1)
        text = m.group(2)
        if "effects" in path.lower() or text.startswith("Effect:") or text.startswith("Effect "):
            return f"\n\n> [!danger] {format_effect_title(text)}\n\n"
        if any(keyword in path.lower() for keyword in ["condition", "action", "spell", "bestiary-ability"]):
            cond_match = re.match(r"^(Stunned|Frightened|Sickened|Slowed|Grabbed|Restrained|Clumsy|Drained|Doomed|Enfeebled|Wounded|Dying)\s+(\d+)$", text, re.IGNORECASE)
            if cond_match:
                return f"[[{cond_match.group(1)}]] {cond_match.group(2)}"
            display_map = {
                "steps": "Step", "step": "Step",
                "strides": "Stride", "stride": "Stride",
                "strikes": "Strike", "strike": "Strike",
                "grabs": "Grab", "grab": "Grab"
            }
            mapped = display_map.get(text.lower())
            if mapped:
                return f"[[{mapped}|{text}]]"
            return f"[[{text}]]"
        return text

    html = re.sub(r"@UUID\[([^\]]+)\]\{([^\}]+)\}", replace_uuid, html)
    
    # Replace UUID links without text
    def replace_uuid_no_text(m):
        path = m.group(1)
        last = path.split(".")[-1]
        name = last.replace("-", " ")
        if re.match(r"^[a-zA-Z0-9]{16}$", name):
            return ""
        if "effects" in path.lower() or name.startswith("Effect:") or name.startswith("Effect "):
            return f"\n\n> [!danger] {format_effect_title(name)}\n\n"
        return f"[[{name}]]"
        
    html = re.sub(r"@UUID\[([^\]]+)\]", replace_uuid_no_text, html)
    
    # Strip any remaining HTML tags
    html = re.sub(r"<[^>]+>", "", html)
    # Format degrees of success as bullet points
    html = re.sub(
        r"(?m)^(?:\s*[-\*]?\s*)?\*\*(Critical Success|Critical Failure|Success|Failure)\*\*",
        r"- **\1**",
        html
    )
    # Clean up double newlines
    html = re.sub(r"\n{3,}", "\n\n", html)
    return html.strip()

def format_iwr(iwr_list, name):
    parts = []
    for item in iwr_list:
        i_type = item.get("type", "").replace("-", " ")
        i_val = item.get("value", "")
        exceptions = item.get("exceptions", [])
        exceptions_str = ""
        if exceptions:
            exceptions_str = " except " + ", ".join(e.replace("-", " ") for e in exceptions)
        
        val_str = f" {i_val}" if i_val != "" else ""
        parts.append(f"{i_type}{val_str}{exceptions_str}")
    if parts:
        return f" **{name}** " + ", ".join(parts)
    return ""

def parse_spellcasting(items):
    spellcasting_list = []
    entries = [i for i in items if i.get("type") == "spellcastingEntry"]
    spells = [i for i in items if i.get("type") == "spell"]
    
    for entry in entries:
        entry_id = entry.get("_id")
        entry_name = entry.get("name", "")
        system = entry.get("system", {})
        
        spelldc = system.get("spelldc", {})
        dc = spelldc.get("dc", 0)
        attack_val = spelldc.get("value", 0)
        prepared_val = system.get("prepared", {}).get("value", "")
        
        desc_parts = [f"DC {dc}, attack +{attack_val}"]
        entry_spells = [s for s in spells if s.get("system", {}).get("location", {}).get("value") == entry_id]
        spells_by_rank = {}
        
        if prepared_val == "prepared":
            slots = system.get("slots", {})
            for slot_key, slot_data in slots.items():
                if not slot_key.startswith("slot"):
                    continue
                try:
                    rank = int(slot_key.replace("slot", ""))
                except:
                    continue
                prepared_list = slot_data.get("prepared", [])
                rank_spells = []
                for p in prepared_list:
                    p_id = p.get("id")
                    spell_item = next((s for s in entry_spells if s.get("_id") == p_id), None)
                    if spell_item:
                        rank_spells.append(spell_item)
                if rank_spells:
                    spells_by_rank[rank] = rank_spells
        else:
            for s in entry_spells:
                try:
                    rank = int(s.get("system", {}).get("level", {}).get("value", 0))
                except:
                    rank = 0
                spells_by_rank.setdefault(rank, []).append(s)
        
        rank_strings = []
        for rank in sorted(spells_by_rank.keys(), reverse=True):
            rank_spells = spells_by_rank[rank]
            spell_links = []
            for s in rank_spells:
                s_name = s.get("name", "")
                suffixes = [" (At Will)", " (Constant)"]
                link_str = f"[[{s_name}]]"
                for suff in suffixes:
                    if s_name.endswith(suff):
                        base_name = s_name[:-len(suff)]
                        link_str = f"[[{base_name}]]{suff}"
                        break
                spell_links.append(link_str)
            
            spells_str = ", ".join(spell_links)
            if rank == 0:
                rank_strings.append(f"**Cantrips** {spells_str}")
            else:
                slot_info = ""
                if prepared_val in ["prepared", "spontaneous"]:
                    try:
                        max_slots = int(system.get("slots", {}).get(f"slot{rank}", {}).get("max", 0))
                    except:
                        max_slots = 0
                    if max_slots > 0:
                        slot_info = f" ({max_slots} slots)"
                
                rank_strings.append(f"**{ordinal(rank)}**{slot_info} {spells_str}")
        
        if rank_strings:
            spellcasting_list.append({
                "name": entry_name,
                "desc": "; ".join(desc_parts) + "<br>" + "<br>".join(rank_strings)
            })
            
    return spellcasting_list

def parse_abilities(items):
    abilities_top = []
    abilities_mid = []
    abilities_bot = []
    attacks = []
    
    def get_sort_key(x):
        try:
            return int(x.get("sort", 0))
        except:
            return 0
    sorted_items = sorted(items, key=get_sort_key)
    for item in sorted_items:
        i_type = item.get("type", "")
        name = item.get("name", "")
        system = item.get("system", {})
        
        if i_type == "melee":
            bonus = system.get("bonus", {}).get("value", 0)
            sign = "+" if bonus >= 0 else ""
            action_icon = "`pf2:1`"
            
            dmg_parts = []
            dmg_rolls = system.get("damageRolls", {})
            for d_key, d_data in dmg_rolls.items():
                damage = d_data.get("damage", "")
                d_type = d_data.get("damageType", "")
                if damage:
                    dmg_parts.append(f"{damage} {d_type}")
            damage_str = " plus ".join(dmg_parts)
            
            traits_val = system.get("traits", {}).get("value", [])
            formatted_traits = []
            is_ranged = False
            for t in traits_val:
                reach_match = re.match(r"^reach-(\d+)$", t)
                range_match = re.match(r"^range-(\d+)$", t)
                range_inc_match = re.match(r"^range-increment-(\d+)$", t)
                if reach_match:
                    formatted_traits.append(f"reach {reach_match.group(1)} ft.")
                elif range_match:
                    formatted_traits.append(f"range {range_match.group(1)} ft.")
                    is_ranged = True
                elif range_inc_match:
                    formatted_traits.append(f"range {range_inc_match.group(1)} ft.")
                    is_ranged = True
                else:
                    formatted_traits.append(t.replace("-", " "))
            
            sys_range = system.get("range")
            if sys_range:
                is_ranged = True
                if isinstance(sys_range, dict):
                    inc = sys_range.get("increment")
                    if inc and f"range {inc} ft." not in formatted_traits:
                        formatted_traits.append(f"range {inc} ft.")
            
            traits_str = ", ".join(formatted_traits)
            traits_display = f" ({traits_str})" if traits_str else ""
            strike_name = "Ranged strike" if is_ranged else "Melee strike"
            
            effects_list = system.get("attackEffects", {}).get("value", [])
            custom_effect = system.get("attackEffects", {}).get("custom", "")
            effects_parts = []
            for eff in effects_list:
                clean_eff = eff.replace("lich-", "").replace("-", " ").title()
                effects_parts.append(f"[[{clean_eff}]]")
            if custom_effect:
                effects_parts.append(custom_effect)
            effects_str = " plus ".join(effects_parts)
            effects_display = f" plus {effects_str}" if effects_str else ""
            
            desc = f"{name} {sign}{bonus} ({action_icon}){traits_display}, **Damage** {damage_str}{effects_display}"
            attacks.append({
                "name": strike_name,
                "desc": desc
            })
            
        elif i_type == "action":
            if should_exclude_ability(name):
                continue
            action_type = system.get("actionType", {}).get("value", "passive")
            category = system.get("category", "")
            raw_desc = system.get("description", {}).get("value", "")
            desc = clean_html(raw_desc)
            
            action_val = system.get("actions", {}).get("value")
            prefix = ""
            if action_val in [1, "1"]:
                prefix = "`pf2:1` "
            elif action_val in [2, "2"]:
                prefix = "`pf2:2` "
            elif action_val in [3, "3"]:
                prefix = "`pf2:3` "
            elif action_type == "reaction":
                prefix = "`pf2:r` "
            elif action_type == "free":
                prefix = "`pf2:0` "
            
            ability_desc = prefix + desc
            is_reaction = (action_type == "reaction")
            is_defensive = (category == "defensive")
            has_trigger = ("**trigger**" in ability_desc.lower())
            is_aura = ("(aura)" in name.lower() or "aura" in raw_desc.lower() and action_type == "passive")
            
            if is_reaction or is_defensive or has_trigger:
                abilities_mid.append({"name": name, "desc": ability_desc})
            elif action_type == "passive" or is_aura:
                abilities_top.append({"name": name, "desc": ability_desc})
            else:
                abilities_bot.append({"name": name, "desc": ability_desc})
                
    return abilities_top, abilities_mid, abilities_bot, attacks

def generate_frontmatter(data):
    lines = []
    lines.append("---")
    lines.append("type: creature")
    
    group_str = ", ".join(f'"{g}"' for g in data["group"])
    lines.append(f"group: [{group_str}]")
    lines.append("statblock: true")
    lines.append("layout: Basic Pathfinder 2e Layout")
    lines.append(f'name: "{data["name"]}"')
    lines.append(f'level: "{data["level"]}"')
    lines.append(f'rare_01: "{data["rare_01"]}"')
    lines.append('rare_02: ""')
    lines.append('rare_03: ""')
    lines.append('rare_04: ""')
    lines.append(f'alignment: "{data["alignment"]}"')
    lines.append(f'size: "{data["size"]}"')
    
    for i in range(1, 8):
        val = data.get(f"trait_{i:02d}", "")
        lines.append(f'trait_{i:02d}: "{val}"')
        
    lines.append("perception:")
    lines.append("  - name: Perception")
    lines.append(f'    desc: "{data["perception"]}"')
    lines.append(f'languages: "{data["languages"]}"')
    
    lines.append("skills:")
    lines.append("  - name: Skills")
    lines.append(f'    desc: "{data["skills"]}"')
    
    ab_mods_str = ", ".join(f'"{m}"' for m in data["abilityMods"])
    lines.append(f"abilityMods: [{ab_mods_str}]")
    
    def append_list(label, items):
        if not items:
            lines.append(f"{label}: []")
        else:
            lines.append(f"{label}:")
            for item in items:
                i_name = item["name"].replace('"', '\\"')
                i_desc = item["desc"].replace('"', '\\"')
                i_desc = i_desc.replace("\n", " <br> ")
                lines.append(f'  - name: "{i_name}"')
                lines.append(f'    desc: "{i_desc}"')
                
    append_list("abilities_top", data["abilities_top"])
    
    lines.append("armorclass:")
    lines.append("  - name: AC")
    ac_desc = data["ac"].replace('"', '\\"')
    lines.append(f'    desc: "{ac_desc}"')
    
    lines.append("health:")
    lines.append("  - name: HP")
    hp_desc = data["hp"].replace('"', '\\"')
    lines.append(f'    desc: "{hp_desc}"')
    
    append_list("abilities_mid", data["abilities_mid"])
    lines.append(f'speed: "{data["speed"]}"')
    append_list("attacks", data["attacks"])
    append_list("spellcasting", data["spellcasting"])
    append_list("abilities_bot", data["abilities_bot"])
    
    lines.append(f'sourcebook: "{data["sourcebook"]}"')
    lines.append(f'source-type: "{data["source-type"]}"')
    lines.append("---")
    
    return "\n".join(lines)

def process_file_data(raw_data, sourcebook, level):
    system = raw_data.get("system", {})
    name = raw_data.get("name", "")
    
    rarity_raw = system.get("traits", {}).get("rarity", "common")
    rare_01 = rarity_raw.capitalize()
    size_raw = system.get("traits", {}).get("size", {}).get("value", "med")
    size = SIZE_MAP.get(size_raw, "Medium")
    
    traits_list = system.get("traits", {}).get("value", [])
    capitalized_traits = [t.capitalize() for t in traits_list if t != rarity_raw]
    
    trait_dict = {}
    for i in range(1, 8):
        val = capitalized_traits[i-1] if i-1 < len(capitalized_traits) else ""
        trait_dict[f"trait_{i:02d}"] = val
        
    group = capitalized_traits[:2]
    if not group:
        group = ["Humanoid"]
        
    perception_mod = format_mod(system.get("perception", {}).get("mod", 0))
    senses = system.get("perception", {}).get("senses", [])
    senses_parts = []
    for s in senses:
        raw_type = s.get("type", "")
        s_type_clean = raw_type.replace("-", " ").title()
        if s_type_clean.lower() == "low light vision":
            s_type_clean = "Low-Light Vision"
        s_type = f"[[{s_type_clean}]]"
        s_acuity = s.get("acuity", "")
        s_range = s.get("range", "")
        acuity_str = f" ({s_acuity})" if s_acuity else ""
        range_str = f" {s_range} feet" if s_range else ""
        senses_parts.append(f"{s_type}{acuity_str}{range_str}")
    senses_str = ", ".join(senses_parts)
    perception_desc = f"{perception_mod}" + (f"; {senses_str}" if senses_str else "")
    
    lang_val = system.get("details", {}).get("languages", {}).get("value", [])
    lang_details = system.get("details", {}).get("languages", {}).get("details", "")
    languages_str = ", ".join(l.capitalize() for l in lang_val)
    if lang_details:
        languages_str += f" ({lang_details})" if languages_str else lang_details
        
    skills_dict = system.get("skills", {})
    skills_list = []
    for sk_key, sk_data in skills_dict.items():
        sk_name = sk_key.capitalize()
        sk_val = sk_data.get("base", 0)
        skills_list.append(f"{sk_name} {format_mod(sk_val)}")
        
    items = raw_data.get("items", [])
    for item in items:
        if item.get("type") == "lore":
            l_name = item.get("name", "")
            l_val = item.get("system", {}).get("mod", {}).get("value", 0)
            skills_list.append(f"{l_name} {format_mod(l_val)}")
            
    skills_str = ", ".join(skills_list)
    
    abilities = system.get("abilities", {})
    ability_mods = [
        format_mod(abilities.get("str", {}).get("mod", 0)),
        format_mod(abilities.get("dex", {}).get("mod", 0)),
        format_mod(abilities.get("con", {}).get("mod", 0)),
        format_mod(abilities.get("int", {}).get("mod", 0)),
        format_mod(abilities.get("wis", {}).get("mod", 0)),
        format_mod(abilities.get("cha", {}).get("mod", 0)),
    ]
    
    ac_val = system.get("attributes", {}).get("ac", {}).get("value", 10)
    ac_details = system.get("attributes", {}).get("ac", {}).get("details", "")
    saves = system.get("saves", {})
    fort_val = format_mod(saves.get("fortitude", {}).get("value", 0))
    fort_detail = saves.get("fortitude", {}).get("saveDetail", "")
    fort_str = f"{fort_val} {fort_detail}".strip()
    
    ref_val = format_mod(saves.get("reflex", {}).get("value", 0))
    ref_detail = saves.get("reflex", {}).get("saveDetail", "")
    ref_str = f"{ref_val} {ref_detail}".strip()
    
    will_val = format_mod(saves.get("will", {}).get("value", 0))
    will_detail = saves.get("will", {}).get("saveDetail", "")
    will_str = f"{will_val} {will_detail}".strip()
    
    ac_desc = f"{ac_val}" + (f" {ac_details}" if ac_details else "") + f"; **Fort** {fort_str}, **Ref** {ref_str}, **Will** {will_str}"
    
    hp_max = system.get("attributes", {}).get("hp", {}).get("max", 1)
    hp_details = system.get("attributes", {}).get("hp", {}).get("details", "")
    hp_str = f"{hp_max}"
    if hp_details:
        hp_str += f"; {hp_details}"
        
    imm_str = format_iwr(system.get("attributes", {}).get("immunities", []), "Immunities")
    weak_str = format_iwr(system.get("attributes", {}).get("weaknesses", []), "Weaknesses")
    res_str = format_iwr(system.get("attributes", {}).get("resistances", []), "Resistances")
    
    if imm_str: hp_str += f";{imm_str}"
    if weak_str: hp_str += f";{weak_str}"
    if res_str: hp_str += f";{res_str}"
    
    speed_val = system.get("speed", {}).get("value", 0)
    speed_str = f"{speed_val} feet"
    other_speeds = system.get("speed", {}).get("otherSpeeds", [])
    for ospeed in other_speeds:
        s_type = ospeed.get("type", "")
        s_val = ospeed.get("value", 0)
        speed_str += f", {s_type} {s_val} feet"
        
    abilities_top, abilities_mid, abilities_bot, attacks = parse_abilities(items)
    spellcasting = parse_spellcasting(items)
    
    pub_notes = system.get("details", {}).get("publicNotes", "")
    blurb = system.get("details", {}).get("blurb", "")
    desc_html = pub_notes if pub_notes else blurb
    description = clean_html(desc_html)
    
    out_data = {
        "name": name,
        "level": level,
        "group": group,
        "rare_01": rare_01,
        "alignment": "",
        "size": size,
        "perception": perception_desc,
        "languages": languages_str,
        "skills": skills_str,
        "abilityMods": ability_mods,
        "abilities_top": abilities_top,
        "ac": ac_desc,
        "hp": hp_str,
        "abilities_mid": abilities_mid,
        "speed": speed_str,
        "attacks": attacks,
        "spellcasting": spellcasting,
        "abilities_bot": abilities_bot,
        "sourcebook": sourcebook,
        "source-type": "Remaster"
    }
    out_data.update(trait_dict)
    
    frontmatter = generate_frontmatter(out_data)
    
    note_content = f"""{frontmatter}
### `= this.file.name`

{description}

```statblock
creature: "{name}"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
"""
    return note_content

def standardize_newlines(text):
    if not text:
        return ""
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").split("\n")]
    return "\n".join(lines).strip()

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Import and update creatures from Foundry VTT.")
    parser.add_argument("--write", action="store_true", help="Perform the actual write and update operations")
    args = parser.parse_args()

    # Sync the repository first
    sync_repository()

    # Load localization database
    load_localization()
    
    # Scan files
    print("Scanning Foundry VTT packs...")
    foundry_files = []
    for root, dirs, files in os.walk(PF2E_PACKS_DIR):
        for f in files:
            if f.endswith(".json") and f != "_folders.json":
                foundry_files.append(os.path.join(root, f))
                
    print(f"Found {len(foundry_files)} total JSON files in compendiums.")
    
    new_entities = []
    updated_entities = []
    unchanged_count = 0
    ignored_count = 0
    
    for filepath in foundry_files:
        try:
            with open(filepath, "r") as fh:
                raw_data = json.load(fh)
                
            if raw_data.get("type") != "npc":
                ignored_count += 1
                continue
                
            system = raw_data.get("system", {})
            pub = system.get("details", {}).get("publication", {})
            title = pub.get("title", "")
            
            sourcebook = ""
            if "monster core 2" in title.lower():
                sourcebook = "Monster Core 2"
            elif "monster core" in title.lower():
                sourcebook = "Monster Core"
            elif "npc core" in title.lower():
                sourcebook = "NPC Core"
            elif "player core" in title.lower():
                sourcebook = "Player Core"
            elif "gm core" in title.lower():
                sourcebook = "GM Core"
            else:
                ignored_count += 1
                continue
                
            name = raw_data.get("name", "")
            level = str(system.get("details", {}).get("level", {}).get("value", 0))
            
            safe_name = name.replace(":", "_").replace("?", "_").replace("/", "_").replace("\\", "_")
            dest_filepath = os.path.join(OUTPUT_DIR, f"Level {level}", f"{safe_name}.md")
            
            new_content = process_file_data(raw_data, sourcebook, level)
            if not new_content:
                ignored_count += 1
                continue
                
            if not os.path.exists(dest_filepath):
                new_entities.append((name, dest_filepath, new_content))
            else:
                with open(dest_filepath, "r") as fh:
                    existing_content = fh.read()
                    
                if standardize_newlines(existing_content) != standardize_newlines(new_content):
                    updated_entities.append((name, dest_filepath, new_content))
                else:
                    unchanged_count += 1
                    
        except Exception as e:
            print(f"Error checking {os.path.basename(filepath)}: {e}")
            
    print("\n" + "="*40)
    print("IMPORT STATUS REPORT")
    print("="*40)
    print(f"New Entities to Create: {len(new_entities)}")
    print(f"Entities to Update:     {len(updated_entities)}")
    print(f"Unchanged Entities:     {unchanged_count}")
    print(f"Ignored/Unsupported:    {ignored_count}")
    print("="*40)
    
    if not args.write:
        if new_entities:
            print("\nNew Entities (first 10 shown):")
            for name, path, _ in new_entities[:10]:
                print(f" - [NEW] {name} -> {os.path.basename(path)}")
            if len(new_entities) > 10:
                print(f" ... and {len(new_entities) - 10} more.")
        if updated_entities:
            print("\nUpdated/Modified Entities (first 10 shown):")
            for name, path, _ in updated_entities[:10]:
                print(f" - [UPDATE] {name} -> {os.path.basename(path)}")
            if len(updated_entities) > 10:
                print(f" ... and {len(updated_entities) - 10} more.")
        print("\nDry Run completed. Run with `--write` to write the updates to your vault.")
        return
        
    if new_entities or updated_entities:
        print("\nWriting changes to the vault...")
        created_count = 0
        updated_count = 0
        
        for name, path, content in new_entities:
            try:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w") as fh:
                    fh.write(content)
                created_count += 1
            except Exception as e:
                print(f"Error creating {name}: {e}")
                
        for name, path, content in updated_entities:
            try:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w") as fh:
                    fh.write(content)
                updated_count += 1
            except Exception as e:
                print(f"Error updating {name}: {e}")
                
        print(f"\nSuccessfully created {created_count} new files and updated {updated_count} existing files.")
    else:
        print("\nNo changes to write. All entities are up-to-date!")

if __name__ == "__main__":
    main()
