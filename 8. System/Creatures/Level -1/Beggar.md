---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Beggar"
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
    desc: "+3"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +3, Deception +3, Diplomacy +3, Stealth +5, Underworld Lore +2"
abilityMods: ["+1", "+3", "+2", "+0", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "14; **Fort** +4, **Ref** +7, **Will** +3"
health:
  - name: HP
    desc: "10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+1 bludgeoning"
  - name: "Melee strike"
    desc: "Rock +5 (`pf2:1`) (thrown 10), **Damage** 1d4+1 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Beat a Retreat"
    desc: "`pf2:2` The beggar Strides three times and gains a +2 circumstance bonus to AC during those actions."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Wherever there is poverty, there are beggars. Beggars are truly the downtrodden of society-folks who have been cast out into the streets due to a variety of setbacks or the weight of circumstance. Some beggars work for underworld organizations as lookouts, spies, or even hired muscle on the cheap-sometimes by choice, but often not.

Unfortunately, every society has people living on its fringes. While good communities work to grant aid and respite to their downtrodden, sometimes-due to economic downturn, famine, or war-the ranks of the less fortunate exceed the community's capacity to support them. In heartless neutral and evil societies, poverty is seen as an inevitability that can never be truly eradicated, or even worse, as a tool to be manipulated for political gain.

```statblock
creature: "Beggar"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
