---
type: creature
group: ["Amphibious", "Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Krooth"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Amphibious"
trait_02: "Animal"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Low-Light Vision]], [[Scent]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +18, Stealth +18, Survival +17"
abilityMods: ["+6", "+3", "+6", "-4", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "26; **Fort** +20, **Ref** +17, **Will** +14"
health:
  - name: HP
    desc: "150"
abilities_mid:
  - name: "+4 Status to All Saves vs. Fear"
    desc: ""
  - name: "Pain Frenzy"
    desc: "Whenever the krooth is damaged by a critical hit, it gains a +2 status bonus to attack and damage rolls until the end of its next turn. It can't use reactions while this frenzy lasts. <br>  <br> > [!danger] Effect: Pain Frenzy"
  - name: "Reactive Strike (Tail Only)"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (deadly d10, poison, reach 10 ft., unarmed), **Damage** 2d12+9 piercing plus [[Poison Tooth]]"
  - name: "Melee strike"
    desc: "Claw +20 (`pf2:1`) (agile, unarmed), **Damage** 2d8+9 slashing"
  - name: "Melee strike"
    desc: "Tail +20 (`pf2:1`) (reach 15 ft.), **Damage** 2d8+9 piercing"
spellcasting: []
abilities_bot:
  - name: "Aquatic Ambush"
    desc: "`pf2:1` 40 feet <br>  <br> **Requirements** The monster is hiding in water and a creature that hasn't detected it is within the listed number of feet. <br>  <br> **Effect** The monster moves up to its swim Speed + 10 feet toward the triggering creature, traveling on water and on land. Once the creature is in reach, the monster makes a Strike against it. The creature is [[Off-Guard]] against this Strike."
  - name: "Poison Tooth"
    desc: "`pf2:1` **Requirements** The krooth damaged a creature with its jaws on its most recent action this turn; <br>  <br> **Effect** The krooth snaps off one of its teeth in the creature it hit. The creature takes 1d6 persistent bleed damage and is [[Drained]] 1. Neither can be healed while the tooth remains. <br>  <br> Removing the tooth safely requires a successful DC 26 [[Medicine]] check to [[Administer First Aid]]. Instead of ending bleeding or stabilizing, this removes the tooth and the drained condition, but it doesn't automatically end the bleed damage."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Krooths, sometimes called crocodile eaters, are fast and vicious hunters of bogs and wetlands. While they are known to hunt and eat crocodiles, alligators, and virtually any creature with flesh, their favorite prey are lizardfolk, boggards, and dinosaurs.

Krooths are found alone or in packs. Male krooths are solitary and territorial creatures—fierce, bold, and bloodthirsty. Female krooths, on the other hand, are more likely to shy away from potential predators but swiftly turn violent when their brood is threatened. Because their offspring are so vulnerable, female krooths gather in packs to raise their young, sending smaller groups to hunt for food while the rest of the pack watches the brood. Krooths mate only once every 4 or 5 years, and the mating process is a curiously gruesome spectacle. An entire pack of females will hunt as a group for a lone male krooth, claiming their prize in a frenzy that can last for an entire day and night. After the mating has finished, the females slay their mate and devour his nutrientrich flesh, and his organs in particular. These organs contain a unique chemical compound vital to gestation. Many naturalists will pay handsomely for the fresh remains of a male krooth so they can study the strange properties of the creature's blood and organs. In addition, krooths have poisonous, hollow teeth. When these creatures bite their prey, a tooth breaks off and causes the victim to bleed profusely as their blood pours through the hollow tooth.

Whether male or female, krooths seem to be repelled by goblinoid flesh, especially that of bugbears. This doesn't mean krooths won't kill goblinoids, especially those threatening their young, but they typically do so using only their claws and tails, and they take great care to clean themselves thoroughly after such a killing.

```statblock
creature: "Krooth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
