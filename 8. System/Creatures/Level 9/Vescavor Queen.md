---
type: creature
group: ["Fiend", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vescavor Queen"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]]"
languages: "Chthonian"
skills:
  - name: Skills
    desc: "Acrobatics +20, Athletics +18, Religion +16, Stealth +20, Survival +16"
abilityMods: ["+6", "+5", "+5", "+1", "+3", "+2"]
abilities_top:
  - name: "Rage Pheromones"
    desc: "If the vescavor queen's spit Strike damages a creature, it takes a –2 status penalty to all saving throws imposed by vescavor swarms for 1 minute."
armorclass:
  - name: AC
    desc: "28; **Fort** +17, **Ref** +19, **Will** +15"
health:
  - name: HP
    desc: "150; **Weaknesses** cold iron 10, holy 10; **Resistances** acid 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (magical, unarmed, unholy), **Damage** 1d10+13 piercing plus 1d10 acid"
  - name: "Melee strike"
    desc: "Claw +20 (`pf2:1`) (agile, magical, reach 10 ft., unarmed, unholy), **Damage** 2d10+8 slashing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Stinger +20 (`pf2:1`) (magical, reach 15 ft., unholy), **Damage** 2d4 piercing plus 2d10 acid"
  - name: "Ranged strike"
    desc: "Spit +19 (`pf2:1`) (acid, magical, range 30 ft.), **Damage** 2d8 acid plus [[Rage Pheromones]]"
spellcasting: []
abilities_bot:
  - name: "Chaotic Spawning"
    desc: "`pf2:3` The vescavor queen strengthens her swarms. All vescavor swarms within @Template[emanation|distance:100]{100 feet} become Huge and [[Quickened]] for 1 minute. Vescavor swarms can only use the extra action each round for the Ravenous Bites action. <br>  <br> > [!danger] Effect: Chaotic Spawning"
  - name: "Feeding Time"
    desc: "`pf2:1` The vescavor queen causes any number of vescavor swarms within 100 feet to immediately use their reaction to perform the Ravenous Bites action."
  - name: "Opportune Snack"
    desc: "`pf2:1` The vescavor queen pulls a creature it has [[Grabbed]] or [[Restrained]] into a space adjacent to it and makes a jaws Strike with a +2 circumstance bonus."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A vescavor queen is a horrifying sight. Much like their swarms, they resemble an acrid green wasp, but their abdomens are abnormally bloated and covered in acid-leaking spikes; their mouths make up the majority of their face and are filled with large, gnarled teeth, each the size of a human finger. They only possess one pair of arms, each the length of their entire body but abnormally folded and kept close, and their five pairs of wings are unnaturally stacked upon each other in a way that would make flight impossible for any natural creature. These queens ensure that the swarms never end their dreadful march towards wherever food can be found. Not only will they gradually create vescavor swarms, but they can also cause existing swarms to double in number at a moment's notice. These strengthened swarms are also blessed with increased vigor and speed. Moreover, a queen's acidic spit is laced with pheromones that drive her swarms into a rage, which she uses to direct the swarms towards priority targets.

Occasionally, a powerful fiend will capture a vescavor queen and use her to create swarms in a controlled environment. However, the practice was quickly abandoned. For all the damage these swarms might cause to a fiendish master's enemies, it is rarely worth the cost of keeping the queen and her endless swarms of children fed and under control. Even keeping the queen in one location can be costly and difficult, as it is almost impossible to find a cage that a queen cannot eat her way out of, given sufficient time.

These gluttonous green vermin travel from the Outer Rifts in an endless search for food. Along the way, these acrid wasps devour everything in sight. Not even the ground itself is spared from their appetite. While any single vescavor is no problem, they travel in swarms to overwhelm anything trying to stop them. In a truly unfortunate situation, several swarms will be gathered and led by a vescavor queen. These queens, while fearsome on their own, can drive their brood into a feeding rage unlike any other. Swarms found without a queen are directionless, destroying anything around them indiscriminately.

Whenever a vescavor swarm is not eating, it gibbers mind-numbing songs from the fiends' dark world. Adapted to the shrieking jungles of their home plane, they issue a call that confuses and corrupts mortals.

Philosophers who ponder the Outer Rifts often conjecture as to what kind of soul forms a vescavor. The idea of insect souls being sent to the Outer Rifts is often laughed off but never entirely dismissed. Some assume that they are demons of gluttony, plain and simple. Some of the more creative explanations of vescavor origins posit that all the bits of soul eaten up by attacking demons are what coalesce into these endless swarms. Such an explanation would account for how these endlessly feeding demons also seem to be endless in number.

```statblock
creature: "Vescavor Queen"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
