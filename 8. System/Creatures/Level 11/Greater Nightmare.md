---
type: creature
group: ["Beast", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Greater Nightmare"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Beast"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]]"
languages: "Chthonian, Daemonic, Diabolic"
skills:
  - name: Skills
    desc: "Acrobatics +23, Athletics +24, Intimidation +22, Survival +20"
abilityMods: ["+7", "+4", "+5", "+2", "+5", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "31; **Fort** +25, **Ref** +24, **Will** +21"
health:
  - name: HP
    desc: "200; **Resistances** fire 15"
abilities_mid:
  - name: "Smoke"
    desc: "20 feet. <br>  <br> The nightmare continually exhales black smoke. Creatures within the aura are [[Concealed]] to those outside it, and creatures outside the aura are concealed to creatures within it. Nightmares and their riders can see through this smoke. <br>  <br> A creature that begins its turn in the area must succeed at a DC 28 [[Fortitude]] save or be [[Sickened]] 2. It's then temporarily immune to being sickened by the smoke for 1 minute. This is an inhaled poison, and the nightmare and its rider are immune to it."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +24 (`pf2:1`) (magical, reach 10 ft., unarmed, unholy), **Damage** 3d10+13 piercing"
  - name: "Melee strike"
    desc: "Hoof +24 (`pf2:1`) (agile, fire, magical, unholy), **Damage** 2d8+10 bludgeoning plus 2d6 fire"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30, attack +22<br>**7th** [[Interplanar Teleport (Self and Rider Only)]]"
abilities_bot:
  - name: "Flaming Gallop"
    desc: "`pf2:2` The nightmare Strides or Flies up to triple its Speed. Its hooves burst with intense flame, dealing 6d6 fire damage with a DC 30 [[Reflex]] save to each creature other than the nightmare's rider that the nightmare moves adjacent to during its gallop. Each creature can be affected only once during a single use of Flaming Gallop."
  - name: "Trample"
    desc: "`pf2:3` Large or smaller, hoof, DC 30 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The enormous greater nightmare is valued for its ability to invade other realities with its rider.

Nightmares are flaming equine harbingers of death.

```statblock
creature: "Greater Nightmare"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
