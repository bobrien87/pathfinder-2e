---
type: creature
group: ["Mindless", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Severed Head"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Mindless"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +4"
abilityMods: ["+1", "+2", "+0", "-5", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +4, **Ref** +6, **Will** +4"
health:
  - name: HP
    desc: "7; void healing; **Immunities** bleed, death effects, disease, paralyzed, poison, unconscious; **Weaknesses** vitality 1"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +6 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d4+1 piercing"
spellcasting: []
abilities_bot:
  - name: "Gnash"
    desc: "`pf2:1` **Requirements** The beheaded's previous action was a jaws Strike that dealt damage to its target. <br>  <br> **Effect** The severed head makes a second jaws Strike as it violently shakes itself, trying to rip away a mouthful of flesh. On a success, the target takes an additional 1d4 slashing damage and 1 persistent bleed damage."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The most common beheaded appears simply as a rotting head, barely preserved by the magic that created it.

Beheaded are the reanimated heads of decapitation victims. These mindless undead fly through the air or roll around to attack their prey.

```statblock
creature: "Severed Head"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
