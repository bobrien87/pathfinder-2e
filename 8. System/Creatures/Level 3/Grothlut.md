---
type: creature
group: ["Aberration", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Grothlut"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +11"
abilityMods: ["+4", "-2", "+4", "-5", "+0", "-3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +11, **Ref** +5, **Will** +7"
health:
  - name: HP
    desc: "50; **Immunities** acid"
abilities_mid:
  - name: "Disgusting Demise"
    desc: "When the grothlut is reduced to 0 Hit Points, its digestive organs rupture, unleashing alchemical acid and poison upon all creatures in a @Template[emanation|distance:30]. Each creature in the area must succeed at a DC 19 [[Fortitude]] save or take @Damage[2d6[acid]|options:area-damage] damage and become [[Sickened]] 1 (double damage and [[Sickened]] 2 on a critical failure)."
  - name: "Piteous Moan"
    desc: "60 feet. <br>  <br> Each nongrothlut creature that enters or starts its turn within the area must succeed at a DC 17 [[Will]] save saving throw or become [[Sickened]] 1 ([[Sickened]] 2 on a critical failure). The creature then becomes temporarily immune for 1 minute. <br>  <br> The grothlut can Dismiss this aura. <br>  <br> A grothlut usually does not begin moaning until it senses the presence of a non-grothlut creature, and it usually stops once it doesn't sense any more such creatures."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +11 (`pf2:1`) (agile, unarmed), **Damage** 1d10+8 slashing"
  - name: "Ranged strike"
    desc: "Digestive Spew +7 (`pf2:1`) (acid, splash, range 15 ft.), **Damage** 2d6 acid plus 1d6 acid"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Sluglike abominations, grothluts are grotesque dregs of the fleshwarping process. While their head and torso are vaguely humanoid, their arms are rubbery and move awkwardly at their sides. Wretched creatures, they moan piteously when other creatures are near, perhaps as the last remnants of their mind pleads to be free from their horrid warped form.

Many fleshwarpers consider the grothlut to be a failure of a creation, as the transformation all but stamps out consciousness. Others disagree, arguing that warping the creature's mind makes it all the more useful, since it becomes pliable and easy to herd. Cultists of Haagenti typically use grothluts as guardians that slowly patrol the edges of their enclaves. Once in position, grothluts can be used as crude shock troops, unleashed to soften enemy forces before more valuable warriors wade in and cut down the enemies who have been nauseated by the grothluts' exploded organs and flesh.

Magical mishaps, divine curses, and untested technology are all capable of wreaking drastic transformations on the body, and are all rampant on the world of Golarion and beyond. Creatures that have undergone changes so drastic they no longer can be considered the same ancestry as they were before are known as fleshwarps. These beings are rare, and their unsettling appearance often provokes horrified responses from other people.

Some creatures revel in the total degradation of their defeated foes through fleshwarping. Though the technique was originally taught to mortals by the demon lord Haagenti, mortals have spent eons modifying and perfecting the method. Fleshcrafters torture their enemies in vats of churning magical reagents, reshaping their flesh and psyche alike into horrid and monstrous things.

```statblock
creature: "Grothlut"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
