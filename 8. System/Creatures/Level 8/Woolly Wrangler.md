---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Woolly Wrangler"
level: "8"
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
    desc: "+16"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +14, Intimidation +14, Nature +16, Survival +18, Mountain Lore +18"
abilityMods: ["+6", "+3", "+4", "+0", "+2", "+2"]
abilities_top:
  - name: "In Balance"
    desc: "Whenever the woolly wrangler rolls a success on a [[Recall Knowledge]] check using Nature or Mountain Lore, they get a critical success instead."
armorclass:
  - name: AC
    desc: "26; **Fort** +19, **Ref** +12, **Will** +16"
health:
  - name: HP
    desc: "125; **Resistances** cold 10"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Uneven Footing"
    desc: "10 feet. <br>  <br> While the woolly wrangler is mounted on a Huge or Gargantuan creature, the ground near the mount shakes and buckles. Squares in the aura are difficult terrain for Medium or smaller creatures."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greatclub +20 (`pf2:1`) (backswing, magical, shove), **Damage** 2d10+12 bludgeoning"
  - name: "Melee strike"
    desc: "Whip +19 (`pf2:1`) (disarm, nonlethal, reach, trip), **Damage** 1d4+12 slashing"
  - name: "Melee strike"
    desc: "Fist +19 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+12 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Wrangling Whip"
    desc: "`pf2:2` The woolly wrangler makes a whip Strike. On a hit, the woolly wrangler can either knock the target [[Prone]] or pull it up to 5 feet. If the creature ends this movement adjacent to the wrangler's mount, the mount can make a melee unarmed Strike against the creature as a free action."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

When a giant, dangerous animal is found, there's always someone who tries to pet it. A woolly wrangler is usually accompanied by an [[Elephant]] or [[Mammoth]]. They can Command this Animal without needing to succeed at a Nature check.

Explorers are often well-equipped and well-trained for any type of hazard and are eager to lead others into the wild.

```statblock
creature: "Woolly Wrangler"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
