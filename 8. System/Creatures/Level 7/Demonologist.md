---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Demonologist"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15"
languages: "Chthonian, Common"
skills:
  - name: Skills
    desc: "Arcana +16, Diplomacy +11, Religion +15, Academia Lore +14, Demon Lore +18"
abilityMods: ["+3", "+1", "+2", "+4", "+4", "+0"]
abilities_top:
  - name: "Demonic Temptation"
    desc: "Demonic study has garnered the attention of at least one demon who is actively trying to possess the demonologist. When the demonologist publicly espouses the benefits of demonic power (whether they believe it a good thing or not), they gain a +1 status bonus to skill checks, AC, and saves for 1 day. These bonuses don't apply against demons. At the end of the day, the demonologist must attempt a DC 20 [[Will]] save, becoming possessed for 1 day on a failure (or permanently on a critical failure)."
  - name: "Demon Summoning"
    desc: "The demonologist can cast a 5th-rank [[Summon Fiend]] arcane spell to summon a demon. To do so, they must sacrifice two 4th-rank prepared spells and voluntarily take 4d12 mental damage that can't be reduced or prevented. If the demonologist is unable to Sustain the Spell, including if they're knocked out or killed, the spell continues, but the GM rolls a DC 10 flat check each round, ending the spell on a failure."
armorclass:
  - name: AC
    desc: "22; **Fort** +13, **Ref** +12, **Will** +15"
health:
  - name: HP
    desc: "100"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longspear +17 (`pf2:1`) (magical, reach), **Damage** 1d8+9 piercing"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+9 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 25, attack +17<br>**4th** (3 slots) [[Clairvoyance]], [[Dispelling Globe]], [[Wall of Fire]]<br>**3rd** (4 slots) [[Acid Grip]], [[Fireball]], [[Grease]], [[Slow]]<br>**2nd** (4 slots) [[Blur]], [[Environmental Endurance]], [[Laughing Fit]], [[See the Unseen]]<br>**1st** (4 slots) [[Fear]], [[Fear]], [[Fleet Step]], [[Mending]]<br>**Cantrips** [[Caustic Blast]], [[Daze]], [[Detect Magic]], [[Light]], [[Read Aura]]"
abilities_bot:
  - name: "Breach the Outer Rifts"
    desc: "`pf2:0` **Requirements** The demonologist's last action was to cast a non-cantrip spell <br>  <br> **Effect** The demonologist siphons energy drawn from the Outer Rifts into their weapon. Until the end of the turn, the weapon deals an extra 2d6 damage. <br>  <br> Roll 1d20 to determine the type: <br>  <br> - 1–7 acid <br> - 8–9 cold <br> - 10–11 electricity <br> - 12–18 fire <br> - 19–20 void."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Demonologists can pull a creature from the Outer Rifts and bend it to their will... for a time.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

```statblock
creature: "Demonologist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
