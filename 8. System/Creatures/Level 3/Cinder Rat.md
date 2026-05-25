---
type: creature
group: ["Elemental", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cinder Rat"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +10, Stealth +10, Survival +9"
abilityMods: ["+2", "+3", "+2", "-4", "+2", "+0"]
abilities_top:
  - name: "Smoke Vision"
    desc: "The cinder rat ignores the [[Concealed]] condition from smoke."
armorclass:
  - name: AC
    desc: "18; **Fort** +9, **Ref** +12, **Will** +6"
health:
  - name: HP
    desc: "45; **Immunities** bleed, fire, paralyzed, poison, sleep; **Weaknesses** cold 5, water 5"
abilities_mid:
  - name: "Fetid Fumes"
    desc: "5 feet. <br>  <br> A creature that enters the aura or begins its turn there must succeed at a DC 22 [[Fortitude]] save or become [[Sickened]] 1. <br>  <br> Everything within the aura, including the cinder rat, is [[Concealed]] by smoke."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`) (finesse, unarmed), **Damage** 1d8+4 fire plus 1d4 fire"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These oversized rodents are made of smoldering charcoal and elemental fire, and noxious fumes continually bellow from their flaming flesh. Even other fire elementals find cinder rats unpleasant and are glad when they're summoned away from the Plane of Fire.

Fire elementals are destructive manifestations of the scorching Plane of Fire. Although most fire elementals revel in the chance to experience new kinds of fires away from their home plane, even the most considerate fire elemental can be a danger to humanoids and their property.

```statblock
creature: "Cinder Rat"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
