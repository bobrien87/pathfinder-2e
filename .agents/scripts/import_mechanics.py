import os
import json
import re
import sys
import subprocess

# Define source directories and target directories
PF2E_DIR = "/Users/personal/.gemini/antigravity/pf2e"
PF2E_PACKS_DIR = os.path.join(PF2E_DIR, "packs/pf2e")
LANG_FILE = os.path.join(PF2E_DIR, "static/lang/en.json")
VAULT_DIR = "/Users/personal/Obsidian Vaults/Pathfinder 2e"

LOCALIZATION_DICT = {}
FLAT_LOCALIZATION_DICT = {}

REMASTER_TITLES = [
    "pathfinder player core",
    "pathfinder player core 2",
    "pathfinder gm core",
    "pathfinder monster core",
    "pathfinder monster core 2",
    "pathfinder npc core"
]

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

def flatten_dict(d, parent_key="", sep="."):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def load_localization():
    global LOCALIZATION_DICT, FLAT_LOCALIZATION_DICT
    try:
        with open(LANG_FILE, "r") as fh:
            LOCALIZATION_DICT = json.load(fh)
        FLAT_LOCALIZATION_DICT = flatten_dict(LOCALIZATION_DICT)
        print("Successfully loaded localization database.")
    except Exception as e:
        LOCALIZATION_DICT = {}
        FLAT_LOCALIZATION_DICT = {}
        print(f"Warning: could not load localization file: {e}")

def get_localization(key):
    # Try flat dict first
    if key in FLAT_LOCALIZATION_DICT:
        return FLAT_LOCALIZATION_DICT[key]
    
    # Fallback to nested walk
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

def standardize_newlines(text):
    if not text:
        return ""
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").split("\n")]
    return "\n".join(lines).strip()

def clean_empty_frontmatter(note_content):
    parts = note_content.split("---", 2)
    if len(parts) < 3:
        return note_content
    fm_lines = parts[1].split("\n")
    cleaned_fm_lines = []
    for line in fm_lines:
        if not line.strip():
            continue
        m = re.match(r"^([^:]+):\s*(.*)$", line)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip()
            # Keep 'type' even if empty, skip other empty fields
            if key != "type" and val in ['""', '"[]"', '[]', 'None', '"None"', 'null', '"null"', "''", '"{}"', '{}']:
                continue
        cleaned_fm_lines.append(line)
    parts[1] = "\n" + "\n".join(cleaned_fm_lines) + "\n"
    return "---".join(parts)

def is_remaster_entity(data):
    pub = data.get("system", {}).get("publication", {})
    title = pub.get("title", "").lower()
    remaster = pub.get("remaster", False)
    
    # Check remaster flag
    if remaster:
        return True
        
    # Check if core remaster book title matches
    if any(bt in title for bt in REMASTER_TITLES):
        return True
        
    # Special Deity exception
    if data.get("type") == "deity" and "divine mysteries" in title:
        return True
        
    return False

# FORMATTERS
def format_traits(traits):
    if not traits:
        return "[]"
    val = traits.get("value", [])
    rarity = traits.get("rarity", "")
    traits_list = []
    for t in val:
        if t != rarity:
            traits_list.append(f"[[{t.replace('-', ' ').capitalize()}]]")
    if not traits_list:
        return "[]"
    return json.dumps(traits_list)

def format_rarity(traits):
    if not traits:
        return ""
    rarity = traits.get("rarity", "")
    if rarity and rarity != "common":
        return rarity.capitalize()
    return ""

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

def format_boosts(boosts_dict):
    if not boosts_dict:
        return ""
    parts = []
    for key in sorted(boosts_dict.keys(), key=lambda x: int(x) if x.isdigit() else 99):
        val = boosts_dict[key].get("value", [])
        custom = boosts_dict[key].get("custom", "")
        if val:
            parts.append("/".join(v.capitalize() for v in val if v))
        elif custom:
            parts.append(custom)
    return ", ".join(parts)

def format_prereqs(prereqs):
    if not prereqs:
        return ""
    val = prereqs.get("value", [])
    if isinstance(val, list):
        parts = []
        for item in val:
            if isinstance(item, dict):
                parts.append(item.get("value", ""))
            else:
                parts.append(str(item))
        return ", ".join(p for p in parts if p)
    return str(val)

def format_frequency(freq):
    if not freq:
        return ""
    val = freq.get("value", 1)
    per = freq.get("per", "")
    if per:
        per_clean = per.replace("-", " ")
        if val == 1:
            return f"once per {per_clean}"
        elif val == 2:
            return f"twice per {per_clean}"
        else:
            return f"{val} times per {per_clean}"
    return ""

def format_cast(time_val):
    if not time_val:
        return ""
    t_str = str(time_val).lower().strip()
    if t_str == "1" or t_str == "one-action":
        return "`pf2:1`"
    elif t_str == "2" or t_str == "two-actions":
        return "`pf2:2`"
    elif t_str == "3" or t_str == "three-actions":
        return "`pf2:3`"
    elif t_str == "reaction":
        return "`pf2:r`"
    elif t_str == "free" or t_str == "free-action":
        return "`pf2:0`"
    return t_str

def format_area(area):
    if not area:
        return ""
    if isinstance(area, dict):
        val = area.get("value", "")
        a_type = area.get("type", "").replace("-", " ")
        if val and a_type:
            return f"{val}-foot {a_type}"
        return str(val or a_type)
    return str(area)

def format_defense(defense):
    if not defense:
        return ""
    if isinstance(defense, dict):
        save = defense.get("save", {})
        if save:
            stat = save.get("statistic", "").capitalize()
            basic = "basic " if save.get("basic") else ""
            if stat:
                return f"{basic}{stat}"
        return defense.get("value", "")
    return str(defense)

def format_duration(duration):
    if not duration:
        return ""
    if isinstance(duration, dict):
        val = duration.get("value", "")
        sustained = "sustained" if duration.get("sustained") else ""
        if val and sustained:
            return f"{val} ({sustained})"
        return val or sustained
    return str(duration)

def format_price(price):
    if not price:
        return ""
    if isinstance(price, dict):
        gp = price.get("gp", 0)
        sp = price.get("sp", 0)
        cp = price.get("cp", 0)
        parts = []
        if gp: parts.append(f"{gp} gp")
        if sp: parts.append(f"{sp} sp")
        if cp: parts.append(f"{cp} cp")
        if parts:
            return ", ".join(parts)
        val = price.get("value", "")
        if val:
            return str(val)
    return str(price)

def format_bulk(bulk):
    if not bulk:
        return "—"
    if isinstance(bulk, dict):
        val = bulk.get("value", 0)
        if val == 0:
            return "—"
        if abs(val - 0.1) < 0.01:
            return "L"
        return str(val)
    return str(bulk)

def format_activation(activation):
    if not activation:
        return ""
    if isinstance(activation, dict):
        time_val = activation.get("time", {}).get("value", "")
        if time_val:
            icon = format_cast(time_val)
            components = activation.get("components", {})
            comp_str = ""
            if components:
                comp_list = [k.capitalize() for k, v in components.items() if v]
                if comp_list:
                    comp_str = f" ({', '.join(comp_list)})"
                return f"{icon}{comp_str}"
            return icon
    return ""

def format_mod(val):
    try:
        val = int(val)
        return f"+{val}" if val >= 0 else str(val)
    except:
        return str(val)

def get_val_str(obj, key):
    val = obj.get(key)
    if val is None:
        return ""
    if isinstance(val, dict):
        return str(val.get("value", ""))
    return str(val)

def format_stealth(stealth):
    if not stealth:
        return ""
    if isinstance(stealth, dict):
        val = stealth.get("value")
        details = stealth.get("details", "")
        if details:
            return details
        if val is not None:
            return format_mod(val)
    return str(stealth)

def format_domains(domains):
    if not domains:
        return ""
    parts = []
    for item in domains:
        if isinstance(item, str):
            parts.append(item.split(".")[-1].capitalize())
        elif isinstance(item, dict):
            parts.append(item.get("name", "").capitalize())
    return ", ".join(parts)

def format_divine_spells(spells_dict):
    if not spells_dict:
        return ""
    parts = []
    for rank, spell_uuid in sorted(spells_dict.items(), key=lambda x: int(x[0])):
        spell_name = spell_uuid.split(".")[-1].replace("-", " ").title()
        parts.append(f"Rank {rank}: [[{spell_name}]]")
    return ", ".join(parts)

# ENTITY PARSERS
def parse_ancestry(data):
    system = data.get("system", {})
    size_map = {"tiny": "Tiny", "sm": "Small", "med": "Medium", "lg": "Large", "huge": "Huge", "grg": "Gargantuan"}
    size_raw = system.get("size", "med")
    size = size_map.get(size_raw.lower(), "Medium")
    
    desc = clean_html(system.get("description", {}).get("value", ""))
    # Strip trailing ancestry name link: *Name*, *[[Name]]*, plain Name, or [[Name]]
    desc = re.sub(r"\n+\*?(?:\[\[[^\]]+\]\]|[A-Z][a-zA-Z ]+)\*?\s*$", "", desc)
    # Remove wrapping italic from entire description (some are fully wrapped in <em>)
    desc = re.sub(r"^\*(.*)\*$", r"\1", desc, flags=re.DOTALL)
    speed_raw = system.get("speed", 25)
    speed = str(speed_raw.get("value", 25)) if isinstance(speed_raw, dict) else str(speed_raw)
    
    note = f"""---
type: ancestry
source-type: "Remaster"
rarity: "{format_rarity(system.get("traits", {}))}"
traits: {format_traits(system.get("traits", {}))}
hp: "{system.get("hp", 8)}"
size: "{size}"
speed: "{speed}"
boosts: "{format_boosts(system.get("boosts", {}))}"
flaws: "{format_boosts(system.get("flaws", {}))}"
languages: "{", ".join(l.capitalize() for l in system.get("languages", {}).get("value", []))}"
source: "{system.get("publication", {}).get("title", "")}"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

{desc}

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
"""
    return note

def parse_heritage(data):
    system = data.get("system", {})
    ancestry_dict = system.get("ancestry") or {}
    ancestry_name = ancestry_dict.get("name", "")
    ancestry = f"[[8. System/Character Creation/Ancestries/{ancestry_name}|{ancestry_name}]]" if ancestry_name else "Versatile"
    
    desc = clean_html(system.get("description", {}).get("value", ""))
    
    note = f"""---
type: heritage
source-type: "Remaster"
ancestry: "{ancestry}"
traits: {format_traits(system.get("traits", {}))}
prerequisites: "{format_prereqs(system.get("prerequisites", {}))}"
source: "{system.get("publication", {}).get("title", "")}"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

{desc}

**Source:** `= this.source` (`= this.source-type`)
"""
    return note

def parse_class(data):
    system = data.get("system", {})
    key_ab = [k.capitalize() for k in system.get("keyAbility", {}).get("value", [])]
    key_ab_str = " or ".join(key_ab)
    
    desc = clean_html(system.get("description", {}).get("value", ""))
    
    note = f"""---
type: class
source-type: "Remaster"
traits: {format_traits(system.get("traits", {}))}
key-attribute: "{key_ab_str}"
hp: "{system.get("hp", 8)}"
source: "{system.get("publication", {}).get("title", "")}"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

{desc}

#### Class Features
``` dataview
LIST level
WHERE contains(file.outlinks, this.file.link) AND type = "class-feature"
```

#### Subclasses / Paths
``` dataview
LIST
WHERE contains(file.outlinks, this.file.link) AND type = "subclass"
```

**Source:** `= this.source` (`= this.source-type`)
"""
    return note

def parse_background(data):
    system = data.get("system", {})
    skills_list = []
    ts = system.get("trainedSkills", {})
    for sk in ts.get("value", []):
        skills_list.append(sk.capitalize())
    for lo in ts.get("lore", []):
        skills_list.append(f"{lo} Lore")
    skills = ", ".join(skills_list)
    
    feats_list = []
    items_dict = system.get("items", {})
    for item in items_dict.values():
        feats_list.append(f"[[{item.get('name', '')}]]")
    feats = ", ".join(feats_list)
    
    desc = clean_html(system.get("description", {}).get("value", ""))
    
    note = f"""---
type: background
source-type: "Remaster"
traits: {format_traits(system.get("traits", {}))}
boosts: "{format_boosts(system.get("boosts", {}))}"
skills: "{skills}"
feats: "{feats}"
source: "{system.get("publication", {}).get("title", "")}"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

{desc}

**Source:** `= this.source` (`= this.source-type`)
"""
    return note

def parse_feat(data, archetype_name=None):
    system = data.get("system", {})
    
    archetype_str = f"[[8. System/Character Creation/Archetypes/{archetype_name}|{archetype_name}]]" if archetype_name else ""
    desc = clean_html(system.get("description", {}).get("value", ""))
    
    note = f"""---
type: feat
archetype: "{archetype_str}"
source-type: "Remaster"
level: "{system.get("level", {}).get("value", 1)}"
traits: {format_traits(system.get("traits", {}))}
prerequisites: "{format_prereqs(system.get("prerequisites", {}))}"
access: "{system.get("access", {}).get("value", "")}"
frequency: "{format_frequency(system.get("frequency", {}))}"
trigger: "{get_val_str(system, 'trigger')}"
requirements: "{get_val_str(system, 'requirements')}"
source: "{system.get("publication", {}).get("title", "")}"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

{desc}

**Source:** `= this.source` (`= this.source-type`)
"""
    return note

def parse_archetype(name, dedication_feat):
    system = dedication_feat.get("system", {}) if dedication_feat else {}
    
    prereqs = format_prereqs(system.get("prerequisites", {})) if dedication_feat else ""
    access = system.get("access", {}).get("value", "") if dedication_feat else ""
    source = system.get("publication", {}).get("title", "") if dedication_feat else ""
    
    note = f"""---
type: archetype
source-type: "Remaster"
prerequisites: "{prereqs}"
access: "{access}"
source: "{source}"
---
### `= this.file.name`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "")`

This archetype represents the {name} path. You gain access to its archetype dedication and subsequent feats.

#### Feats
``` dataview
LIST level
WHERE archetype = this.file.link AND lower(type) = "feat"
```

**Source:** `= this.source` (`= this.source-type`)
"""
    return note

def parse_spell(data, sub_type):
    system = data.get("system", {})
    
    desc = clean_html(system.get("description", {}).get("value", ""))
    
    note = f"""---
type: spell
sub-type: "{sub_type}"
source-type: "Remaster"
level: "{system.get("level", {}).get("value", 1)}"
traits: {format_traits(system.get("traits", {}))}
traditions: "{", ".join(t.capitalize() for t in system.get("traditions", {}).get("value", []))}"
cast: "{format_cast(system.get("time", {}).get("value", ""))}"
range: "{system.get("range", {}).get("value", "")}"
area: "{format_area(system.get("area", {}))}"
targets: "{system.get("target", {}).get("value", "")}"
defense: "{format_defense(system.get("defense", {}))}"
duration: "{format_duration(system.get("duration", {}))}"
trigger: "{get_val_str(system, 'trigger')}"
requirements: "{get_val_str(system, 'requirements')}"
source: "{system.get("publication", {}).get("title", "")}"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

{desc}

**Source:** `= this.source` (`= this.source-type`)
"""
    return note

def parse_hazard(data):
    system = data.get("system", {})
    sub_type = "Complex" if system.get("details", {}).get("isComplex", False) else "Simple"
    
    stealth = format_stealth(system.get("attributes", {}).get("stealth", {}))
    disable = clean_html(system.get("attributes", {}).get("disable", {}).get("value", ""))
    
    ac = system.get("attributes", {}).get("ac", {}).get("value", "")
    saves = system.get("saves", {})
    fort = format_mod(saves.get("fortitude", {}).get("value")) if saves.get("fortitude", {}).get("value") is not None else ""
    ref = format_mod(saves.get("reflex", {}).get("value")) if saves.get("reflex", {}).get("value") is not None else ""
    will = format_mod(saves.get("will", {}).get("value")) if saves.get("will", {}).get("value") is not None else ""
    
    hp_max = system.get("attributes", {}).get("hp", {}).get("max", "")
    hp_details = system.get("attributes", {}).get("hp", {}).get("details", "")
    hp = f"{hp_max} {hp_details}".strip() if hp_max else ""
    
    hardness = system.get("attributes", {}).get("hardness", {}).get("value", "")
    immunities = ", ".join(i.replace("-", " ").capitalize() for i in system.get("attributes", {}).get("immunities", []))
    
    desc = clean_html(system.get("description", {}).get("value", ""))
    
    note = f"""---
type: hazard
sub-type: "{sub_type}"
source-type: "Remaster"
level: "{system.get("details", {}).get("level", 1)}"
traits: {format_traits(system.get("traits", {}))}
stealth: "{stealth}"
disable: "{disable}"
ac: "{ac}"
fort: "{fort}"
ref: "{ref}"
will: "{will}"
hp: "{hp}"
hardness: "{hardness}"
immunities: "{immunities}"
reset: "{system.get("attributes", {}).get("reset", {}).get("value", "")}"
source: "{system.get("publication", {}).get("title", "")}"
---
### `= this.file.name`
`= choice(this.sub-type != null and this.sub-type != "", "**Hazard (" + this.sub-type + ")**", "**Hazard**")` `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Stealth** `= this.stealth`
**Disable** `= this.disable`

`= choice(this.ac != null and this.ac != "" or this.fort != null and this.fort != "" or this.ref != null and this.ref != "" or this.will != null and this.will != "", "**AC** " + choice(this.ac != null and this.ac != "", this.ac, "—") + "; **Fort** " + choice(this.fort != null and this.fort != "", "+" + this.fort, "—") + ", **Ref** " + choice(this.ref != null and this.ref != "", "+" + this.ref, "—") + ", **Will** " + choice(this.will != null and this.will != "", "+" + this.will, "—"), "")`
`= choice(this.hp != null and this.hp != "" or this.hardness != null and this.hardness != "", "**HP** " + choice(this.hp != null and this.hp != "", this.hp, "—") + choice(this.hardness != null and this.hardness != "", "; **Hardness** " + this.hardness, "") + choice(this.immunities != null and this.immunities != "", "; **Immunities** " + this.immunities, ""), "")`
`= choice(this.reset != null and this.reset != "", "**Reset** " + this.reset, "")`

{desc}

#### Attacks / Actions
``` dataview
LIST WITHOUT ID action
WHERE file.path = this.file.path
FLATTEN this.attacks as action
```

**Source:** `= this.source` (`= this.source-type`)
"""
    return note

def parse_deity(data):
    system = data.get("system", {})
    sanct_dict = system.get("sanctification") or {}
    sanct = ", ".join(s.capitalize() for s in sanct_dict.get("allowed", []))
    
    align_dict = system.get("alignment") or {}
    align = align_dict.get("own", "")
    
    port_dict = system.get("portfolio") or {}
    portfolio = ", ".join(p.capitalize() for p in port_dict.get("value", []))
    
    dom_dict = system.get("domains") or {}
    domains = format_domains(dom_dict.get("primary", []))
    weapons = ", ".join(w.capitalize() for w in system.get("weapons", []))
    
    font = ", ".join(f.capitalize() for f in system.get("font", []))
    skill = ", ".join(s.capitalize() for s in system.get("skill", []))
    spells = format_divine_spells(system.get("spells", {}))
    
    desc = clean_html(system.get("description", {}).get("value", ""))
    
    note = f"""---
type: deity
source-type: "Remaster"
sanctification: "{sanct}"
alignment: "{align}"
portfolio: "{portfolio}"
domains: "{domains}"
favored-weapon: "{weapons}"
divine-font: "{font}"
divine-skill: "{skill}"
divine-spells: "{spells}"
source: "{system.get("publication", {}).get("title", "")}"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

{desc}

**Source:** `= this.source` (`= this.source-type`)
"""
    return note

def parse_action(data):
    system = data.get("system", {})
    cost = system.get("actions", {}).get("value")
    action_type = system.get("actionType", {}).get("value", "passive")
    
    cast = ""
    if cost in [1, "1"]:
        cast = "`pf2:1`"
    elif cost in [2, "2"]:
        cast = "`pf2:2`"
    elif cost in [3, "3"]:
        cast = "`pf2:3`"
    elif action_type == "reaction":
        cast = "`pf2:r`"
    elif action_type == "free":
        cast = "`pf2:0`"
    else:
        cast = "Passive"
        
    desc = clean_html(system.get("description", {}).get("value", ""))
    
    note = f"""---
type: action
source-type: "Remaster"
traits: {format_traits(system.get("traits", {}))}
cast: "{cast}"
trigger: "{get_val_str(system, 'trigger')}"
requirements: "{get_val_str(system, 'requirements')}"
prerequisites: "{format_prereqs(system.get("prerequisites", {}))}"
source: "{system.get("publication", {}).get("title", "")}"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

{desc}

**Source:** `= this.source` (`= this.source-type`)
"""
    return note

def parse_condition(data):
    system = data.get("system", {})
    desc = clean_html(system.get("description", {}).get("value", ""))
    
    note = f"""---
type: condition
source-type: "Remaster"
traits: {format_traits(system.get("traits", {}))}
source: "{system.get("publication", {}).get("title", "")}"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

{desc}

**Source:** `= this.source` (`= this.source-type`)
"""
    return note

def parse_item(data):
    system = data.get("system", {})
    desc = clean_html(system.get("description", {}).get("value", ""))
    
    note = f"""---
type: item
source-type: "Remaster"
level: "{system.get("level", {}).get("value", 1)}"
traits: {format_traits(system.get("traits", {}))}
price: "{format_price(system.get("price", {}))}"
usage: "{system.get("usage", {}).get("value", "")}"
bulk: "{format_bulk(system.get("bulk", {}))}"
activate: "{format_activation(system.get("activation", {}))}"
source: "{system.get("publication", {}).get("title", "")}"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

{desc}

**Source:** `= this.source` (`= this.source-type`)
"""
    return note

def parse_trait(name, desc):
    note = f"""---
type: trait
source-type: "Remaster"
source: "Pathfinder Core"
---
### `= this.file.name`

{desc}

**Source:** `= this.source` (`= this.source-type`)
"""
    return note

# FILE MANAGEMENT
def clean_filename(name):
    return name.replace(":", "_").replace("?", "_").replace("/", "_").replace("\\", "_").replace("*", "_")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Import Remaster character options and mechanics.")
    parser.add_argument("--write", action="store_true", help="Perform the actual write operations")
    args = parser.parse_args()
    
    # 1. Sync repository
    sync_repository()
    
    # 2. Load localization
    load_localization()
    
    print("Scanning compendiums...")
    
    # Collect all JSON files
    db = {}
    for root, dirs, files in os.walk(PF2E_PACKS_DIR):
        # Determine logical category using path parts relative to PF2E_PACKS_DIR
        rel_path = os.path.relpath(root, PF2E_PACKS_DIR)
        path_parts = rel_path.split(os.sep)
        top_folder = path_parts[0]
        
        if top_folder == "feats":
            if "archetype" in path_parts:
                # E.g. feats/archetype/acrobat
                if len(path_parts) > 2:
                    logical_cat = f"archetype-feat-{path_parts[2]}"
                else:
                    logical_cat = "feat"
            else:
                logical_cat = "feat"
        elif top_folder in ["spells", "actions", "deities", "hazards", "ancestries", "heritages", "classes", "backgrounds", "conditions", "equipment"]:
            logical_cat = top_folder
        else:
            logical_cat = top_folder
            
        for f in files:
            if f.endswith(".json") and f != "_folders.json":
                path = os.path.join(root, f)
                try:
                    with open(path, "r") as fh:
                        data = json.load(fh)
                    data["_file_path"] = path
                    data["_logical_cat"] = logical_cat
                    db.setdefault(logical_cat, []).append(data)
                except:
                    pass

    # We will build list of changes
    import_tasks = [] # list of (dest_path, content, action_type, name)
    
    # 1. Ancestries
    print("Processing Ancestries...")
    for item in db.get("ancestries", []):
        if is_remaster_entity(item):
            name = item["name"]
            content = parse_ancestry(item)
            dest = os.path.join(VAULT_DIR, "8. System/Character Creation/Ancestries", f"{clean_filename(name)}.md")
            import_tasks.append((dest, content, "ancestry", name))
            
    # 2. Heritages
    print("Processing Heritages...")
    for item in db.get("heritages", []):
        if is_remaster_entity(item):
            name = item["name"]
            content = parse_heritage(item)
            dest = os.path.join(VAULT_DIR, "8. System/Character Creation/Heritages", f"{clean_filename(name)}.md")
            import_tasks.append((dest, content, "heritage", name))
            
    # 3. Classes
    print("Processing Classes...")
    for item in db.get("classes", []):
        if is_remaster_entity(item):
            name = item["name"]
            content = parse_class(item)
            dest = os.path.join(VAULT_DIR, "8. System/Character Creation/Classes", f"{clean_filename(name)}.md")
            import_tasks.append((dest, content, "class", name))
            
    # 4. Backgrounds
    print("Processing Backgrounds...")
    for item in db.get("backgrounds", []):
        if is_remaster_entity(item):
            name = item["name"]
            content = parse_background(item)
            dest = os.path.join(VAULT_DIR, "8. System/Character Creation/Backgrounds", f"{clean_filename(name)}.md")
            import_tasks.append((dest, content, "background", name))
            
    # 5. Feats & Archetypes
    print("Processing Feats and Archetypes...")
    
    # We will group archetype feats by their folders
    archetype_folders = {}
    for cat in db.keys():
        if cat.startswith("archetype-feat-"):
            folder_name = cat.replace("archetype-feat-", "")
            archetype_folders[folder_name] = db[cat]
            
    # Process standard feats
    for item in db.get("feat", []):
        if is_remaster_entity(item):
            # Check if it has archetype trait
            traits = item.get("system", {}).get("traits", {}).get("value", [])
            if "archetype" in traits:
                # This goes to Archetypes but is not in a specific folder.
                # We can check if it belongs to an archetype by matching its name/rules
                # or treat it as general archetype feat.
                pass
            name = item["name"]
            content = parse_feat(item)
            dest = os.path.join(VAULT_DIR, "8. System/Character Creation/Feats", f"{clean_filename(name)}.md")
            import_tasks.append((dest, content, "feat", name))
            
    # Process Archetypes & their feats
    for folder_name, feats in archetype_folders.items():
        # Check if archetype has at least one Remaster feat
        remaster_feats = [f for f in feats if is_remaster_entity(f)]
        if not remaster_feats:
            continue
            
        archetype_title = folder_name.replace("-", " ").title()
        
        # Find dedication feat to get prerequisites and access
        dedication_feat = None
        for f in feats:
            if "dedication" in f["name"].lower():
                dedication_feat = f
                break
        if not dedication_feat and remaster_feats:
            dedication_feat = remaster_feats[0]
            
        # Create Archetype Page
        arch_content = parse_archetype(archetype_title, dedication_feat)
        arch_dest = os.path.join(VAULT_DIR, "8. System/Character Creation/Archetypes", f"{clean_filename(archetype_title)}.md")
        import_tasks.append((arch_dest, arch_content, "archetype", archetype_title))
        
        # Create Archetype Feats
        for feat in feats:
            # We import all feats belonging to this archetype if they match the Remaster criteria
            if is_remaster_entity(feat):
                name = feat["name"]
                content = parse_feat(feat, archetype_title)
                dest = os.path.join(VAULT_DIR, "8. System/Character Creation/Feats", f"{clean_filename(name)}.md")
                import_tasks.append((dest, content, "feat", name))
                
    # 6. Spells
    print("Processing Spells...")
    for item in db.get("spells", []):
        if is_remaster_entity(item):
            name = item["name"]
            
            # Determine sub-type and rank
            traits = item.get("system", {}).get("traits", {}).get("value", [])
            is_focus = "focus" in item.get("_file_path", "").lower()
            is_ritual = "ritual" in item.get("_file_path", "").lower()
            is_cantrip = "cantrip" in traits
            
            sub_type = "Spell"
            if is_focus:
                sub_type = "Focus Spell"
            elif is_ritual:
                sub_type = "Ritual"
            elif is_cantrip:
                sub_type = "Cantrip"
                
            rank_val = item.get("system", {}).get("level", {}).get("value", 1)
            rank_folder = f"Rank {rank_val}"
            if is_cantrip:
                rank_folder = "Cantrip"
            elif is_focus:
                rank_folder = "Focus"
            elif is_ritual:
                rank_folder = "Ritual"
                
            content = parse_spell(item, sub_type)
            dest = os.path.join(VAULT_DIR, "8. System/Spells", rank_folder, f"{clean_filename(name)}.md")
            import_tasks.append((dest, content, "spell", name))
            
    # 7. Hazards
    print("Processing Hazards...")
    for item in db.get("hazards", []):
        if is_remaster_entity(item):
            name = item["name"]
            content = parse_hazard(item)
            dest = os.path.join(VAULT_DIR, "8. System/Hazards", f"{clean_filename(name)}.md")
            import_tasks.append((dest, content, "hazard", name))
            
    # 8. Deities
    print("Processing Deities...")
    for item in db.get("deities", []):
        if is_remaster_entity(item):
            name = item["name"]
            content = parse_deity(item)
            dest = os.path.join(VAULT_DIR, "8. System/Rules Reference/Deities", f"{clean_filename(name)}.md")
            import_tasks.append((dest, content, "deity", name))
            
    # 9. Actions
    print("Processing Actions...")
    for item in db.get("actions", []):
        if is_remaster_entity(item):
            name = item["name"]
            content = parse_action(item)
            dest = os.path.join(VAULT_DIR, "8. System/Rules Reference/Actions", f"{clean_filename(name)}.md")
            import_tasks.append((dest, content, "action", name))
            
    # 10. Conditions
    print("Processing Conditions...")
    for item in db.get("conditions", []):
        # Conditions are core rules, always import
        name = item["name"]
        content = parse_condition(item)
        dest = os.path.join(VAULT_DIR, "8. System/Rules Reference/Conditions", f"{clean_filename(name)}.md")
        import_tasks.append((dest, content, "condition", name))
        
    # 11. Items (Equipment & Consumables)
    print("Processing Items (Equipment & Consumables)...")
    for item in db.get("equipment", []):
        if is_remaster_entity(item):
            name = item["name"]
            content = parse_item(item)
            dest = os.path.join(VAULT_DIR, "8. System/Items", f"{clean_filename(name)}.md")
            import_tasks.append((dest, content, "item", name))
                
    # 12. Traits (from en.json)
    print("Processing Traits from en.json...")
    if FLAT_LOCALIZATION_DICT:
        desc_keys = [k for k in FLAT_LOCALIZATION_DICT.keys() if "TraitDescription" in k]
        for dk in desc_keys:
            trait_key_name = dk.split("TraitDescription")[-1]
            desc = clean_html(FLAT_LOCALIZATION_DICT[dk])
            
            # Find a human-readable title
            possible_names = [
                dk.replace("TraitDescription", "Trait"),
                "PF2E.Trait" + trait_key_name,
                "PF2E.WeaponTrait" + trait_key_name,
                "PF2E.ClassTrait" + trait_key_name
            ]
            title = ""
            for pn in possible_names:
                if pn in FLAT_LOCALIZATION_DICT:
                    title = FLAT_LOCALIZATION_DICT[pn]
                    break
            if not title:
                # Format key name e.g. HalfElf -> Half-Elf
                title = re.sub(r"([A-Z])", r" \1", trait_key_name).strip()
                
            content = parse_trait(title, desc)
            dest = os.path.join(VAULT_DIR, "8. System/Rules Reference/Traits", f"{clean_filename(title)}.md")
            import_tasks.append((dest, content, "trait", title))

    # Evaluate action write counts
    new_count = 0
    update_count = 0
    unchanged_count = 0
    write_operations = []
    
    for dest, content, cat, name in import_tasks:
        content = clean_empty_frontmatter(content)
        if not os.path.exists(dest):
            new_count += 1
            write_operations.append((dest, content, "new", name))
        else:
            try:
                with open(dest, "r") as fh:
                    existing = fh.read()
                if standardize_newlines(existing) != standardize_newlines(content):
                    update_count += 1
                    write_operations.append((dest, content, "update", name))
                else:
                    unchanged_count += 1
            except:
                update_count += 1
                write_operations.append((dest, content, "update", name))
                
    print("\n" + "="*40)
    print("MECHANICS IMPORT REPORT")
    print("="*40)
    print(f"New Entities: {new_count}")
    print(f"Updated/Modified: {update_count}")
    print(f"Unchanged: {unchanged_count}")
    print(f"Total Mechanics processed: {len(import_tasks)}")
    print("="*40)
    
    if not args.write:
        if write_operations:
            print("\nProposed Changes (first 10 shown):")
            for path, _, action_type, name in write_operations[:10]:
                print(f" - [{action_type.upper()}] {name} -> {os.path.basename(path)}")
            if len(write_operations) > 10:
                print(f" ... and {len(write_operations) - 10} more.")
        print("\nDry Run completed. Run with `--write` to perform the actual write operations.")
        return
        
    if write_operations:
        print("\nWriting changes to the vault...")
        created_count = 0
        updated_count = 0
        for path, content, action_type, name in write_operations:
            try:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w") as fh:
                    fh.write(content)
                if action_type == "new":
                    created_count += 1
                else:
                    updated_count += 1
            except Exception as e:
                print(f"Error writing {name}: {e}")
        print(f"\nSuccessfully created {created_count} new files and updated {updated_count} existing files.")
    else:
        print("\nNo changes to write. All mechanics are up-to-date!")

if __name__ == "__main__":
    main()
