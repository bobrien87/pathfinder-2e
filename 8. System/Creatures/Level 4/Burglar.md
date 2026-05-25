---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Burglar"
level: "4"
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
    desc: "+10"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +8, Deception +7, Society +7, Stealth +12, Thievery +12, Underworld Lore +7"
abilityMods: ["+2", "+4", "+1", "+1", "+2", "+1"]
abilities_top:
  - name: "+1 Bonus on Perception to Find Traps"
    desc: ""
  - name: "Mobility"
    desc: "When the burglar Strides half their speed or less, that movement does not trigger reactions."
  - name: "Sneak Attack"
    desc: "The burglar deals 1d6 extra precision damage to [[Off Guard]] creatures."
  - name: "Surprise Attack"
    desc: "On the first round of combat, if the burglar rolls Deception or Stealth for initiative, creatures that haven't acted are [[Off Guard]] to them."
armorclass:
  - name: AC
    desc: "21 22 vs. traps; **Fort** +7, **Ref** +12, **Will** +10"
health:
  - name: HP
    desc: "60"
abilities_mid:
  - name: "+1 Circumstance to All Saves vs. Traps"
    desc: ""
  - name: "+1 AC vs. Traps"
    desc: ""
  - name: "Deny Advantage"
    desc: "The burglar isn't [[Off Guard]] to creatures of 4th level or lower that are [[Hidden]], [[Undetected]], flanking, or using [[Surprise Attack]]."
  - name: "Nimble Dodge"
    desc: "`pf2:r` **Trigger** The burglar is targeted with a melee or ranged attack by an attacker it can see. <br>  <br> **Effect** The burglar gains a +2 circumstance bonus to AC against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +14 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+5 piercing"
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Shortbow +14 (`pf2:1`) (deadly d10, propulsive, reload 0, range 60 ft.), **Damage** 1d6+4 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

These criminals specialize in breaking and entering, gaining access to secure buildings and bypassing security measures undetected.

In the underbelly of society, the lawless reign supreme.

```statblock
creature: "Burglar"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
