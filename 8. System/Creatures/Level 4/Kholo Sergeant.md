---
type: creature
group: ["Humanoid", "Kholo"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kholo Sergeant"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Kholo"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Common, Kholo"
skills:
  - name: Skills
    desc: "Athletics +13, Intimidation +9, Stealth +11, Survival +10"
abilityMods: ["+4", "+2", "+2", "+0", "+1", "+0"]
abilities_top:
  - name: "Pack Attack"
    desc: "A kholo sergeant deals 1d4 extra damage to any creature that's within reach of at least two of the kholo sergeant's allies."
  - name: "Rugged Travel"
    desc: "A kholo ignores the first square of difficult terrain they move into each time they Step or Stride."
armorclass:
  - name: AC
    desc: "21; **Fort** +12, **Ref** +10, **Will** +8"
health:
  - name: HP
    desc: "60"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +14 (`pf2:1`) (forceful, sweep), **Damage** 1d6+7 slashing"
  - name: "Melee strike"
    desc: "Jaws +14 (`pf2:1`) (agile, unarmed), **Damage** 1d6+7 piercing"
  - name: "Ranged strike"
    desc: "Composite Shortbow +12 (`pf2:1`) (deadly d10, propulsive, reload 0, range 60 ft.), **Damage** 1d6+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Bark Orders"
    desc: "`pf2:1` The kholo sergeant commands its allies to reposition. Any allies who hear and understand this order can use a reaction to Step."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

When kholos band together to form mercenary bands or raiding parties, the strongest or most respected among them is often designated the hunt leader or sergeant. These kholo are responsible for the safety and success of their packmates and train extensively in the art of war. Their skill at arms makes them powerful adversaries. A kholo sergeant might also serve as a mercenary group's leader in other affairs, such as sorting out domestic disputes or negotiating with rival kholo bands.

Kholo are tall, hyena-headed humanoids who dwell in savannas, warm grasslands, and arid hills. Given their appearance, their affinity for hyenas should not be surprising; kholos share their homes, food, and even many of their behaviors with these animals. Much like hyenas, kholos have a notorious reputation, for much the same reason—their uncanny laughter, frightening intelligence, and efficient pack tactics make them intimidating competition or foes. Kholos are keen to lean into these rumors, using them as a form of psychological warfare against their enemies.

Also like hyenas, kholos prefer to hunt in packs, and are exceptionally skilled at setting up ambushes or separating individual targets from larger groups. As kholo packs value all their members highly, any tactic that gives them an advantage in dangerous situations is seen as virtuous, while chivalry and honor are derided as pointlessly risky. It's a philosophy borne from a deep respect and love for their kholo brethren, but to most other people, it makes kholos terrible neighbors.

Kholos willingly eat nearly any other creature, including dead kholos, which can evoke strong reactions from people and cultures with a taboo against cannibalism or desecrating the dead. To a kholo, it's often more offensive to not eat a dead body, no matter its origin; kholos see no point in wasting precious meat in a harsh and challenging world. Worse still is the refusal to eat the flesh of a dead kholo, which they consider an insult to that kholo's memory and an implication that their flesh is unworthy of consumption. Eating the flesh of honored enemies is, for kholos, a respectful ritual, allowing that being to live on within the pack instead of rotting like trash on the ground.

Kholo women are often larger and stronger than kholo men and are typically considered the leaders of their hunting packs and clans.

```statblock
creature: "Kholo Sergeant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
