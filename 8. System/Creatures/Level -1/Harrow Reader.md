---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Harrow Reader"
level: "-1"
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
    desc: "+7"
languages: "Common"
skills:
  - name: Skills
    desc: "Diplomacy +10, Occultism +5, Performance +5, Society +5, Fortune-Telling Lore +11"
abilityMods: ["+1", "+2", "+1", "+2", "+3", "+3"]
abilities_top:
  - name: "Cold Reading Specialist"
    desc: "For encounters involving fortune-telling, the harrow reader is a 3rd-level challenge."
  - name: "Fated Doom"
    desc: "Though harrow readers try to avoid combat, no throw of the cards can avoid fate, so a harrow reader learns how best to survive. In the harrow reader's first encounter each day, they gain a +1 status bonus to their initiative roll, attack rolls, and AC."
  - name: "Read the Harrow"
    desc: "The harrow reader can conduct a reading over the course of 10 minutes to duplicate the effects of the [[Augury]] spell. The harrow reader can conduct up to five readings per day, but the flat check DC increases by 2. This is cumulative, to a maximum of DC 14 for the fifth."
armorclass:
  - name: AC
    desc: "14; **Fort** +3, **Ref** +6, **Will** +10"
health:
  - name: HP
    desc: "8"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sickle +6 (`pf2:1`) (agile, finesse, trip), **Damage** 1d4+1 slashing"
  - name: "Melee strike"
    desc: "Fist +6 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+1 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A harrow deck is a set of 54 cards with symbolic illustrations that serves as a sacred divining tool. Feared by the superstitious and avoided by those who know better than to tempt fate, many harrow readers live and work in traveling communities, often moving from town to town as opportunities arise.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

```statblock
creature: "Harrow Reader"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
