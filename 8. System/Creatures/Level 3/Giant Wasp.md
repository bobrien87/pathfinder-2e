---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Wasp"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +9"
abilityMods: ["+4", "+4", "+4", "-5", "+1", "+1"]
abilities_top:
  - name: "Giant Wasp Venom"
    desc: "**Saving Throw** DC 19 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** no effect (1 round) <br>  <br> **Stage 2** [[Clumsy]] 2 (1 round) <br>  <br> **Stage 3** [[Paralyzed]] (1 round)"
  - name: "Wasp Larva"
    desc: "**Saving Throw** DC 21 [[Fortitude]] save <br>  <br> **Stage 1** carrier with no ill effect (1d6 days) <br>  <br> **Stage 2** [[Drained]] 1 (1d4 days) <br>  <br> **Stage 3** 5d6 untyped damage, larva emerges (disease ends)"
armorclass:
  - name: AC
    desc: "17; **Fort** +9, **Ref** +11, **Will** +6"
health:
  - name: HP
    desc: "45"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Stinger +12 (`pf2:1`) (poison), **Damage** 1d12+4 piercing plus [[Giant Wasp Venom]]"
spellcasting: []
abilities_bot:
  - name: "Implant Eggs"
    desc: "`pf2:1` The giant wasp lays eggs in an adjacent creature that is [[Paralyzed]] or [[Unconscious]], exposing it to the wasp larva disease."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Giant wasps are much more dangerous but less common than their smaller kin, and—to the relief of those who encounter them—they tend to be solitary.

While the common wasp poses little threat to a hardy adventurer aside from an uncomfortable sting, a large and aggressive swarm of these territorial insects—to say nothing of their oversized kin—can lay low an entire party of heroes. The wasps represented here are of the common variety, also known as yellow jackets, but many other sorts of dangerous wasps exist, such as a Garundi variant that swarms in such great numbers that it can decimate entire villages.

```statblock
creature: "Giant Wasp"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
