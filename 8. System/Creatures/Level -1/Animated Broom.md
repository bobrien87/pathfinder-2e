---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Animated Broom"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+3; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +5"
abilityMods: ["+0", "+1", "+0", "-5", "+0", "-5"]
abilities_top:
  - name: "Dust"
    desc: "A creature hit by an animated broom's bristles must succeed at a DC 15 [[Fortitude]] save or spend its next action coughing. Even if hit by multiple dust attacks, the creature has to spend only 1 action coughing to clear the dust out. <br>  <br> A creature that doesn't breathe is immune to this effect."
armorclass:
  - name: AC
    desc: "15 (13 when broken); construct armor; **Fort** +3, **Ref** +6, **Will** +3"
health:
  - name: HP
    desc: "6"
abilities_mid:
  - name: "Construct Armor (Hardness 2)"
    desc: "Like normal objects, an animated broom has Hardness. This Hardness reduces any damage it takes by an amount equal to the Hardness. Once an animated broom is reduced to less than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks and reducing its Armor Class to 13."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bristles +6 (`pf2:1`) (agile, finesse, magical), **Damage** 1d4 bludgeoning plus [[Dust]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Animated brooms perform menial tasks of cleaning and upkeep, but they can step in to defend a room from intrusion if needed. These simple animated objects can be found with greater frequency than more complicated and costly objects.

Granted a semblance of life through the use of rituals or other strange magic, animated objects take many forms and serve a variety of uses. A few examples of typical animated objects are listed below. Many of these creatures serve as guardians, surprising unsuspecting adventurers when they suddenly attack. Others serve as idle distractions for the exceptionally rich, simple servants created to handle odd jobs, and the like.

```statblock
creature: "Animated Broom"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
