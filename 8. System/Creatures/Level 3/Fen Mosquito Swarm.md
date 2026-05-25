---
type: creature
group: ["Animal", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fen Mosquito Swarm"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
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
    desc: "Acrobatics +6, Stealth +8"
abilityMods: ["+0", "+4", "+3", "-5", "+0", "-5"]
abilities_top:
  - name: "Pyrexic Malaria"
    desc: "The victim can't reduce its [[Sickened]] condition while it's affected by pyrexic malaria <br>  <br> **Saving Throw** DC 20 [[Fortitude]] save <br>  <br> **Onset** 4 days <br>  <br> **Stage 1** [[Sickened]] 1 (1 day) <br>  <br> **Stage 2** [[Enfeebled]] 1 and [[Sickened]] 1 (1 day) <br>  <br> **Stage 3** as stage 2 (1 day) <br>  <br> **Stage 4** [[Unconscious]] (1 day) <br>  <br> **Stage 5** dead"
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +11, **Will** +5"
health:
  - name: HP
    desc: "30; **Immunities** precision, swarm mind; **Weaknesses** area damage 5, splash damage 5; **Resistances** bludgeoning 2, piercing 5, slashing 5"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Swarming Bites"
    desc: "`pf2:1` Each enemy in the swarm's space takes @Damage[1d6[piercing]|options:area-damage] damage (DC 20 [[Reflex]] save) and is exposed to pyrexic malaria. Creatures that fail the saving throw also take 1d4 bleed."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

When deadly fen mosquitoes gather in large numbers, they form into lethal swarms capable of draining blood at a truly alarming rate. Fen mosquito swarms are typically encountered only in tropical swamps or bogs, but during humid months in spring or summer they can drift into riverine areas or even through the waterfront reaches of settlements.

```statblock
creature: "Fen Mosquito Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
