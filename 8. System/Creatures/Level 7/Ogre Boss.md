---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ogre Boss"
level: "7"
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
    desc: "+12; [[Darkvision]]"
languages: "Common, Jotun"
skills:
  - name: Skills
    desc: "Athletics +16, Intimidation +16, Stealth +11"
abilityMods: ["+7", "+0", "+4", "+0", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "25; **Fort** +17, **Ref** +12, **Will** +15"
health:
  - name: HP
    desc: "130"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Sweeping Hook"
    desc: "`pf2:r` **Trigger** The ogre boss successfully [[Trips]] a creature using an ogre hook <br>  <br> **Effect** The ogre boss makes an ogre hook Strike against the creature they tripped."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Ogre Hook +19 (`pf2:1`) (deadly d10, reach 10 ft., trip), **Damage** 1d10+11 piercing"
  - name: "Melee strike"
    desc: "Javelin +12 (`pf2:1`) (thrown 30), **Damage** 1d6+11 piercing"
spellcasting: []
abilities_bot:
  - name: "Bellowing Command"
    desc: "`pf2:1` The ogre boss issues a command to hasten their fellows. Each ogre ally who hears and understands this command becomes [[Quickened]] until the end of that ally's next turn but can use the extra action only to Step or Stride."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

In ogre society, might makes more than right—it makes the rules. The strongest or most violent ogre in a family (in most cases, this is the same ogre) is invariably that family's boss. Quick to hook fallen foes on their weapons, even other ogres fear the repercussions of displeasing an ogre boss. When an ogre boss barks out commands, the other members of the family move quickly to obey.

For many societies, ogres embody brutish, amoral violence and greedy cruelty. Standing 10 feet tall and densely muscled, ogres are usually as strong as they are vicious. The worst ogres are sadists, enjoying remorseless murder, torture, and violence in all of its forms. Although they prefer to vent their violent urges on other humanoids—the smaller the better—ogre captivity can end in a horrifying fate for anyone unlucky enough to fall within their meaty grasp: becoming dinner. But for all their creativity in inflicting pain, ogres often forget that their playthings lack their own robust fortitude and high pain tolerance, and many of their captives die sooner than the ogres might prefer. Meanwhile, those who manage to survive captivity in an ogre's larder often emerge with lasting mental scars. A captive able to keep their wits about them, however, can sometimes trick the brutes by promising treasure, more plentiful food sources, or other crude amusements, taking advantage of an ogre's often-limited intellect to engineer opportunities to escape or gain revenge.

Ogres are social creatures only in the most debased sense. They gather together in groups called families, though members are not always related by blood. The most powerful ogre in any family is the "boss"—usually the family's patriarch or matriarch—whom the other ogres in the family learn to quickly obey or risk being brutalized by the boss's loyal kin. Ogres lair in caves, crumbling ruins, or dilapidated shacks close enough to humanoid settlements or animal trails to make raiding easy. Their lairs are filthy and frequently contain all-too-recognizable evidence of their depravity, along with assorted treasures stolen from past captives.

```statblock
creature: "Ogre Boss"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
