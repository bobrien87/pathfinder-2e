---
type: creature
group: ["Beast", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Nightmare"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Chthonian, Daemonic, Diabolic"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +16, Intimidation +14, Survival +12"
abilityMods: ["+6", "+3", "+3", "+1", "+4", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "24; **Fort** +15, **Ref** +15, **Will** +12"
health:
  - name: HP
    desc: "100; **Resistances** fire 10"
abilities_mid:
  - name: "Smoke"
    desc: "15 feet. <br>  <br> The nightmare continually exhales black smoke. Creatures within the aura are [[Concealed]] to those outside it, and creatures outside the aura are concealed to creatures within it. Nightmares and their riders can see through this smoke. <br>  <br> A creature that begins its turn in the area must succeed at a DC 23 [[Fortitude]] save or be [[Sickened]] 2. It's then temporarily immune to being sickened by the smoke for 1 minute. This is an inhaled poison, and the nightmare and its rider are immune to it."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +16 (`pf2:1`) (magical, unarmed, unholy), **Damage** 2d10+8 piercing"
  - name: "Melee strike"
    desc: "Hoof +16 (`pf2:1`) (agile, fire, magical, unholy), **Damage** 1d8+8 bludgeoning plus 1d6 fire"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 24, attack +16<br>**7th** [[Interplanar Teleport (Self and Rider Only)]]"
abilities_bot:
  - name: "Flaming Gallop"
    desc: "`pf2:2` The nightmare Strides or Flies up to triple its Speed. Its hooves burst with intense flame, dealing 3d6 fire damage with a DC 24 [[Reflex]] save to each creature other than the nightmare's rider that the nightmare moves adjacent to during its gallop. Each creature can be affected only once during a single use of Flaming Gallop."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Nightmares are flaming equine harbingers of death.

```statblock
creature: "Nightmare"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
