---
type: creature
group: ["Incorporeal", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Shadow"
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
  - name: "Shadow Spawn"
    desc: "When a creature's shadow is pulled free by Steal Shadow, it becomes a shadow spawn under the command of the shadow that created it. This [[Shadow Spawn]] doesn't have Steal Shadow and is perpetually and incurably [[Clumsy]] 2. <br>  <br> If the creature the shadow spawn was pulled from dies, the shadow spawn becomes a full-fledged, autonomous shadow. If the creature recovers from its enfeeblement, its shadow returns to it and the shadow spawn is extinguished."
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
abilities_bot:
  - name: "Steal Shadow"
    desc: "`pf2:1` **Requirements** The shadow hit a living creature with a shadow hand Strike on its previous action <br>  <br> **Effect** The shadow pulls at the target's shadow, making the creature [[Enfeebled]] 1. This is cumulative with other enfeebled conditions from shadows, to a maximum of [[Enfeebled]] 4. If this increases a creature's enfeebled value to 3 or more, the target's shadow is separated from its body (see shadow spawn). The enfeebled value from Steal Shadow decreases by 1 every hour."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The mysterious undead known as shadows lurk in dark places and feed on those who stray too far from the light.

```statblock
creature: "Shadow"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
