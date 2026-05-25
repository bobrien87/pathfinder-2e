---
type: creature
group: ["Humanoid", "Kholo"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kholo Hunter"
level: "2"
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
    desc: "+7; [[Darkvision]]"
languages: "Kholo, Common"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +8, Intimidation +4, Stealth +7, Survival +5"
abilityMods: ["+4", "+3", "+2", "-1", "+1", "+0"]
abilities_top:
  - name: "Pack Attack"
    desc: "A kholo hunter deals 1d4 extra damage to any creature that's within reach of at least two of the kholo hunter's allies."
  - name: "Rugged Travel"
    desc: "A kholo ignores the first square of difficult terrain they move into each time they Step or Stride."
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +7, **Will** +7"
health:
  - name: HP
    desc: "29"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Battle Axe +10 (`pf2:1`) (sweep), **Damage** 1d8+4 slashing"
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`) (agile, unarmed), **Damage** 1d8+2 piercing"
  - name: "Ranged strike"
    desc: "Shortbow +10 (`pf2:1`) (deadly d10, range 60 ft.), **Damage** 1d6 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Kholo are tall, hyena-headed humanoids who dwell in savannas, warm grasslands, and arid hills. Given their appearance, their affinity for hyenas should not be surprising; kholos share their homes, food, and even many of their behaviors with these animals. Much like hyenas, kholos have a notorious reputation, for much the same reason—their uncanny laughter, frightening intelligence, and efficient pack tactics make them intimidating competition or foes. Kholos are keen to lean into these rumors, using them as a form of psychological warfare against their enemies.

Also like hyenas, kholos prefer to hunt in packs, and are exceptionally skilled at setting up ambushes or separating individual targets from larger groups. As kholo packs value all their members highly, any tactic that gives them an advantage in dangerous situations is seen as virtuous, while chivalry and honor are derided as pointlessly risky. It's a philosophy borne from a deep respect and love for their kholo brethren, but to most other people, it makes kholos terrible neighbors.

Kholos willingly eat nearly any other creature, including dead kholos, which can evoke strong reactions from people and cultures with a taboo against cannibalism or desecrating the dead. To a kholo, it's often more offensive to not eat a dead body, no matter its origin; kholos see no point in wasting precious meat in a harsh and challenging world. Worse still is the refusal to eat the flesh of a dead kholo, which they consider an insult to that kholo's memory and an implication that their flesh is unworthy of consumption. Eating the flesh of honored enemies is, for kholos, a respectful ritual, allowing that being to live on within the pack instead of rotting like trash on the ground.

Kholo women are often larger and stronger than kholo men and are typically considered the leaders of their hunting packs and clans.

```statblock
creature: "Kholo Hunter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
