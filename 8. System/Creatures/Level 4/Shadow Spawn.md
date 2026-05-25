---
type: creature
group: ["Incorporeal", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Shadow Spawn"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Necril"
skills:
  - name: Skills
    desc: "Acrobatics +10, Stealth +14"
abilityMods: ["-5", "+4", "+0", "-2", "+2", "+3"]
abilities_top:
  - name: "Slink in Shadows"
    desc: "The shadow can [[Hide]] or end its [[Sneak]] in a creature's or object's shadow."
armorclass:
  - name: AC
    desc: "20; **Fort** +8, **Ref** +14, **Will** +12"
health:
  - name: HP
    desc: "40; void healing; **Immunities** death effects, disease, paralyzed, poison, precision, unconscious, bleed; **Resistances** all damage 5 except force, ghost touch, vitality, spirit"
abilities_mid:
  - name: "Light Vulnerability"
    desc: "Attacks against the shadow are treated as magical if made by a creature who is in magical light or with an object that is in magical light (such as from the [[Light]] spell)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shadow Hand +15 (`pf2:1`) (finesse, magical), **Damage** 2d6+3 void"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The mysterious undead known as shadows lurk in dark places and feed on those who stray too far from the light.

```statblock
creature: "Shadow Spawn"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
