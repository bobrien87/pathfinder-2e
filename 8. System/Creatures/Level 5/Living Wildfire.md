---
type: creature
group: ["Elemental", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Living Wildfire"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Pyric"
skills:
  - name: Skills
    desc: "Acrobatics +13"
abilityMods: ["+3", "+4", "+2", "-2", "+3", "+0"]
abilities_top:
  - name: "Smoke Vision"
    desc: "The living wildfire ignores the [[Concealed]] condition from smoke."
armorclass:
  - name: AC
    desc: "22; **Fort** +11, **Ref** +15, **Will** +10"
health:
  - name: HP
    desc: "80; explosion; **Immunities** bleed, fire, paralyzed, poison, sleep; **Weaknesses** cold 5, water 5"
abilities_mid:
  - name: "Explosion"
    desc: "When the living wildfire dies, it explodes, dealing @Damage[3d6[fire]|options:area-damage] damage to each creature in a @Template[emanation|distance:10|traits:fire,damaging-effect] (DC 19 [[Reflex]] save)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tendril +15 (`pf2:1`) (agile, finesse, reach 10 ft.), **Damage** 2d6+6 fire plus 2d4 fire"
  - name: "Ranged strike"
    desc: "Fire Mote +15 (`pf2:1`) (range 60 ft.), **Damage** 2d6+3 fire"
spellcasting: []
abilities_bot:
  - name: "Spreading Flames"
    desc: "`pf2:1` **Requirements** The living wildfire's last action was a Strike that dealt fire damage <br>  <br> **Effect** The fire flares, dealing 3d6 fire damage to each creature adjacent to that target with a DC 19 [[Reflex]] save."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Living wildfires appear as humanoids made of living fire, burning everything they come across for the pure joy of it. Summoners take advantage of this joy and the elementals' explosive ends to spread destruction.

Fire elementals are destructive manifestations of the scorching Plane of Fire. Although most fire elementals revel in the chance to experience new kinds of fires away from their home plane, even the most considerate fire elemental can be a danger to humanoids and their property.

```statblock
creature: "Living Wildfire"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
