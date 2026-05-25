---
type: creature
group: ["Elemental", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ember Fox"
level: "2"
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
    desc: "+8; [[Darkvision]]"
languages: "Pyric (can't speak any language)"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +5, Stealth +8"
abilityMods: ["+1", "+4", "+2", "-2", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +6, **Ref** +10, **Will** +8"
health:
  - name: HP
    desc: "35; **Immunities** bleed, paralyzed, poison, sleep, fire; **Weaknesses** cold 5"
abilities_mid:
  - name: "Cloak in Embers"
    desc: "`pf2:r` **Trigger** An adjacent ally is targeted by an effect that deals fire damage <br>  <br> **Effect** The ember fox drapes itself across its ally, granting the ally fire resistance 10 against the incoming attack. <br>  <br> > [!danger] Effect: Cloak in Embers"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`) (agile, finesse), **Damage** 1d4+3 piercing plus 1d4 fire"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Ember foxes resemble their canid namesakes, save for the flames that make their fur and the tips of their long whiskers flicker and glow. They particularly enjoy hunting elementals from the Plane of Wood.

Destructive manifestations of the Plane of Fire, fire elementals sometimes incorporate burning materials into their being or superheated matter, such as molten rock or searing smoke. In combat, they tend to be aggressive and somewhat reckless. Their attacks can sometimes cause major destruction to the surrounding environment, and many fire elementals seem to enjoy seeing their flames spread far and wide.

```statblock
creature: "Ember Fox"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
