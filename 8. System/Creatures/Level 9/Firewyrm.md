---
type: creature
group: ["Elemental", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Firewyrm"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: "Pyric"
skills:
  - name: Skills
    desc: "Acrobatics +20"
abilityMods: ["+5", "+5", "+4", "-1", "+3", "+0"]
abilities_top:
  - name: "Smoke Vision"
    desc: "The firewyrm ignores the [[Concealed]] condition from smoke."
armorclass:
  - name: AC
    desc: "28; **Fort** +18, **Ref** +20, **Will** +15"
health:
  - name: HP
    desc: "165; explosion; **Immunities** bleed, fire, paralyzed, poison, sleep; **Weaknesses** cold 10, water 10"
abilities_mid:
  - name: "Explosion"
    desc: "When the firewyrm dies, it explodes, dealing @Damage[6d6[fire]|options:area-damage] damage to each creature in a @Template[emanation|distance:10] (DC 28 [[Reflex]] save)."
  - name: "Intense Heat"
    desc: "10 feet. @Damage[4d6[fire]|options:area-damage] damage DC 25 [[Reflex]] save"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tail +20 (`pf2:1`) (reach 15 ft.), **Damage** 2d8+11 fire plus 2d8 fire"
  - name: "Ranged strike"
    desc: "Fire Mote +20 (`pf2:1`) (range 60 ft.), **Damage** 2d8+6 fire"
spellcasting: []
abilities_bot:
  - name: "Breath Fire"
    desc: "`pf2:2` The firewyrm breathes a @Template[cone|distance:30] of fire dealing @Damage[7d6[fire],2d8[persistent,fire]|options:area-damage] damage to every creature within the cone (DC 28 [[Reflex]] save). <br>  <br> The firewyrm can't Breathe Fire again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Firewyrms live in tubes of molten lava found throughout the Plane of Fire. These strange environments often connect to volcanoes on mortal worlds, giving firewyrms access to a wide variety of prey.

Fire elementals are destructive manifestations of the scorching Plane of Fire. Although most fire elementals revel in the chance to experience new kinds of fires away from their home plane, even the most considerate fire elemental can be a danger to humanoids and their property.

```statblock
creature: "Firewyrm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
