---
type: creature
group: ["Plant", "Wood"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Arboreal Warden"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Plant"
trait_02: "Wood"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Low-Light Vision]]"
languages: "Arboreal, Common, Fey"
skills:
  - name: Skills
    desc: "Athletics +13, Stealth +9"
abilityMods: ["+5", "+1", "+3", "+1", "+3", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20 (22 with shield raised); **Fort** +13, **Ref** +9, **Will** +11"
health:
  - name: HP
    desc: "75; **Weaknesses** axe vulnerability 5, fire 10; **Resistances** bludgeoning 5, piercing 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Stone Longsword +13 (`pf2:1`) (reach 10 ft.), **Damage** 1d8+10 bludgeoning"
  - name: "Melee strike"
    desc: "Shield Bash +13 (`pf2:1`), **Damage** 1d6+10 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Shield Push"
    desc: "`pf2:2` The arboreal warden Strides and then makes a shield bash Strike. If the attack hits, the target is pushed 10 feet."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Arboreal wardens are the rangers of arboreal society. These itinerant folk have an innate curiosity about the woodlands in which they dwell, and rarely stop to take root and rest in the same part of the forest twice. This wanderlust makes wardens ideal forest patrollers and scouts. While they are robust combatants, they know better than to confront dangerous foes on their own. Instead, they report any dangers to arboreal regents. In rare cases, large groups of arboreal wardens congregate to form a copse. Copses travel beyond the boundaries of a forest to investigate the hinterlands and gather intelligence on potential threats before returning to report their findings. Arboreal wardens do not pretend to understand to other creatures' motives—like most forces of the natural world, they are ambivalent about mortal affairs that do not involve their forest.

Arboreals are guardians of the forest and representatives of the trees. As long-lived as the woods they watch over, arboreals consider themselves parents and shepherds of trees rather than their gardeners. Consequently, while arboreals tend to be slow and methodical, they are terrifyingly swift when forced to fight in defense of the woods. Though they rarely seek out the companionship of short-lived folk—even elves are fugacious in the eyes of arboreals—and have an inherent distrust of change, arboreals have been known to tolerate those who seek to learn from their long-winded, rambling monologues, especially if such pupils also express a desire to protect the timberlands. Against those who threaten their realm, such as loggers eager to harvest lumber or settlers aiming to establish croplands or a town, arboreals' wrath is unwavering and devastating. Perhaps ironically, arboreals are gifted at tearing down what others build—a trait that serves vengeful members of their kind well.

```statblock
creature: "Arboreal Warden"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
