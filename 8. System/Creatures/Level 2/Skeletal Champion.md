---
type: creature
group: ["Skeleton", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Skeletal Champion"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Skeleton"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +8, Intimidation +7"
abilityMods: ["+4", "+4", "+1", "-1", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "19 (21 with shield raised); **Fort** +5, **Ref** +10, **Will** +6"
health:
  - name: HP
    desc: "25; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Resistances** cold 5, electricity 5, fire 5, piercing 5, slashing 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longsword +10 (`pf2:1`) (versatile p), **Damage** 1d8+4 slashing"
  - name: "Melee strike"
    desc: "Claw +10 (`pf2:1`) (agile, unarmed), **Damage** 1d6+4 slashing"
  - name: "Melee strike"
    desc: "Lance +10 (`pf2:1`) (deadly d8, jousting d6, reach 10 ft.), **Damage** 1d8+4 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These skeletons retain the cunning they possessed in life.

Animated skeletons are among the most common types of undead.

```statblock
creature: "Skeletal Champion"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
