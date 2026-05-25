---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ogre Warrior"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: "Jotun"
skills:
  - name: Skills
    desc: "Athletics +12, Intimidation +9"
abilityMods: ["+5", "-1", "+4", "-2", "+0", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +11, **Ref** +6, **Will** +5"
health:
  - name: HP
    desc: "50"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Ogre Hook +12 (`pf2:1`) (deadly d10, reach 10 ft., trip), **Damage** 1d10+7 piercing"
  - name: "Melee strike"
    desc: "Javelin +6 (`pf2:1`) (thrown 30), **Damage** 1d6+7 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The simplest of ogres are slabs of muscle with hateful eyes, misshapen visages, and malformed bodies. Always eager for mayhem and murder, ogre warriors are quick to turn on their kin when there's a shortage of smaller folk to torment, so those who lead ogres do their best to keep them constantly distracted with new opportunities for raids and ruin.

For many societies, ogres embody brutish, amoral violence and greedy cruelty. Standing 10 feet tall and densely muscled, ogres are usually as strong as they are vicious. The worst ogres are sadists, enjoying remorseless murder, torture, and violence in all of its forms. Although they prefer to vent their violent urges on other humanoids—the smaller the better—ogre captivity can end in a horrifying fate for anyone unlucky enough to fall within their meaty grasp: becoming dinner. But for all their creativity in inflicting pain, ogres often forget that their playthings lack their own robust fortitude and high pain tolerance, and many of their captives die sooner than the ogres might prefer. Meanwhile, those who manage to survive captivity in an ogre's larder often emerge with lasting mental scars. A captive able to keep their wits about them, however, can sometimes trick the brutes by promising treasure, more plentiful food sources, or other crude amusements, taking advantage of an ogre's often-limited intellect to engineer opportunities to escape or gain revenge.

Ogres are social creatures only in the most debased sense. They gather together in groups called families, though members are not always related by blood. The most powerful ogre in any family is the "boss"—usually the family's patriarch or matriarch—whom the other ogres in the family learn to quickly obey or risk being brutalized by the boss's loyal kin. Ogres lair in caves, crumbling ruins, or dilapidated shacks close enough to humanoid settlements or animal trails to make raiding easy. Their lairs are filthy and frequently contain all-too-recognizable evidence of their depravity, along with assorted treasures stolen from past captives.

```statblock
creature: "Ogre Warrior"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
