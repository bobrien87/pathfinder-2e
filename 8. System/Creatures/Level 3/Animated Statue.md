---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Animated Statue"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +11"
abilityMods: ["+4", "-2", "+5", "-5", "+0", "-5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "19 (15 when broken); construct armor; **Fort** +12, **Ref** +5, **Will** +5"
health:
  - name: HP
    desc: "35"
abilities_mid:
  - name: "Construct Armor (Hardness 6)"
    desc: "Like normal objects, an animated statue has Hardness. This Hardness reduces any damage it takes by an amount equal to the Hardness. Once an animated statue is reduced to less than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks and its Armor Class is reduced to 15."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (magical, unarmed), **Damage** 1d8+6 bludgeoning plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Animated statues are often used to guard crypts, small shrines, or areas in government buildings where they can be positioned amid normal statues to hide their true nature until an intruder arouses their ire. Many less scrupulous adventurers, fueled by paranoia that statues will animate and attack, smash any statues they encounter, ruining harmless, ancient relics.

Granted a semblance of life through the use of rituals or other strange magic, animated objects take many forms and serve a variety of uses. A few examples of typical animated objects are listed below. Many of these creatures serve as guardians, surprising unsuspecting adventurers when they suddenly attack. Others serve as idle distractions for the exceptionally rich, simple servants created to handle odd jobs, and the like.

```statblock
creature: "Animated Statue"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
