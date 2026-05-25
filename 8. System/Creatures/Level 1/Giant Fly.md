---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Fly"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]], [[Tremorsense]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +6"
abilityMods: ["+3", "+4", "+3", "-5", "+3", "-5"]
abilities_top:
  - name: "Fly Pox"
    desc: "A giant fly could carry any disease, but most transmit a virulent but not fatal infection called fly pox with their bite <br>  <br> **Saving Throw** DC 16 [[Fortitude]] save <br>  <br> **Onset** 1 day <br>  <br> **Stage 1** [[Enfeebled]] 1 (1 day) <br>  <br> **Stage 2** as stage 1 (1 day) <br>  <br> **Stage 3** [[Enfeebled]] 2 (1 day) <br>  <br> **Stage 4** as stage 3 (1 day) <br>  <br> **Stage 5** enfeebled 2 and [[Fatigued]] (1 day)"
armorclass:
  - name: AC
    desc: "16; **Fort** +6, **Ref** +9, **Will** +6"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "Avoid the Swat"
    desc: "`pf2:r` **Trigger** The giant fly is targeted with a melee or ranged attack by an attacker it can see <br>  <br> **Effect** The giant fly gains a +2 circumstance bonus to AC against the triggering attack. If the attack misses, the giant insect can Fly up to its fly Speed."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandibles +8 (`pf2:1`), **Damage** 1d6+3 piercing plus [[Fly Pox]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

This massive fly's twitching limbs seem to never stop moving as it constantly cleans itself and scoops anything edible into its mouthparts. While primarily carrion eaters, giant flies sometimes prey on livestock or other animals too slow to get away. They are not particularly dangerous, and are mostly reviled due to their obnoxious droning and habit of spreading disease.

Giant flies are pony-sized insects that have massive compound eyes and bodies bristling with short, stiff hairs. Their lairs are notorious for the rotting meat they stockpile to lay their eggs in. Their maggot dens are also prime breeding grounds for virulent diseases.

```statblock
creature: "Giant Fly"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
