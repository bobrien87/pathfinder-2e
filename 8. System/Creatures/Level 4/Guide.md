---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Guide"
level: "4"
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
    desc: "+14"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +12, Nature +8, Stealth +10, Survival +12, Scouting Lore +12"
abilityMods: ["+4", "+1", "+2", "+1", "+3", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20; **Fort** +14, **Ref** +8, **Will** +11"
health:
  - name: HP
    desc: "60"
abilities_mid:
  - name: "Guide's Warning"
    desc: "`pf2:r` **Trigger** The guide is about to roll a Perception or Survival check to determine their initiative <br>  <br> **Effect** The guide visually or audibly warns allies, granting them a +1 circumstance bonus to their initiative rolls. This bonus increases to +2 if the guide was [[Scouting]]. Depending on how the guide warns allies, this action has the auditory or visual trait. <br>  <br> > [!danger] Effect: Guide's Warning"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greataxe +12 (`pf2:1`) (sweep), **Damage** 1d12+8 slashing"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Shortbow +9 (`pf2:1`) (deadly d10, propulsive, reload 0, range 60 ft.), **Damage** 1d6+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Guiding Words"
    desc: "`pf2:1` The guide points out a weakness of a creature within 30 feet. Until the start of the guide's next turn, the guide and all allies that can hear the guiding words gain a +1 circumstance bonus to attack rolls against that creature, and the guide's Strikes deal an extra 1d4 precision damage to that creature. <br>  <br> > [!danger] Effect: Guiding Words (Guide)"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Guides bring travelers, tourists, and adventurers into the wondrous natural world, using their expertise to avoid deadly monsters and gruesome hazards.

Explorers are often well-equipped and well-trained for any type of hazard and are eager to lead others into the wild.

```statblock
creature: "Guide"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
