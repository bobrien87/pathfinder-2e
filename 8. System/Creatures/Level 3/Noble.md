---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Noble"
level: "3"
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
    desc: "+11"
languages: "Common"
skills:
  - name: Skills
    desc: "Deception +10, Diplomacy +10, Intimidation +9, Society +10, Games Lore +8"
abilityMods: ["+2", "+3", "+1", "+1", "+2", "+4"]
abilities_top:
  - name: "Lip Reader"
    desc: "After years of sticking their nose where it doesn't belong, the noble has learned to read lips from afar. If they're trying to read lips in an encounter or attempting a difficult feat of lip reading, they are [[Fascinated]] and [[Off Guard]], and might need to succeed at a [[Society]] check with a DC determined by the GM."
  - name: "Sneak Attack"
    desc: "The noble deals an additional 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +10, **Will** +11"
health:
  - name: HP
    desc: "50"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +10 (`pf2:1`) (deadly d8, disarm, finesse), **Damage** 1d6+6 piercing"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Noble's Ruse"
    desc: "`pf2:1` **Frequency** Once per round <br>  <br> **Effect** The noble Feints. On a success, the noble Strikes the target."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Envied by many and detested by some, nobles exude confidence and gentility. Gossip and gambling are often nobles' favorite pastimes. Dayto-day life for a noble is usually a mixture of business and leisure, and to an onlooker, such a lifestyle can appear to be nothing more than a string of meals, parties, and game halls.

The denizens of a noble court are the most powerful people in a civilization, primed with wealth, station, and authority above the common people.

```statblock
creature: "Noble"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
