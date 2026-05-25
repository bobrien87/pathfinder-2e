---
type: creature
group: ["Elemental", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Elemental Inferno"
level: "11"
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
    desc: "+20; [[Darkvision]]"
languages: "Pyric"
skills:
  - name: Skills
    desc: "Acrobatics +21"
abilityMods: ["+6", "+6", "+5", "+0", "+3", "+0"]
abilities_top:
  - name: "Smoke Vision"
    desc: "The elemental inferno ignores the [[Concealed]] condition from smoke."
  - name: "Blue Flames"
    desc: "When the elemental inferno scores a critical hit, its body surges with blue flames, increasing the damage of its intense heat and Inferno Leap by 3d6 until the start of its next turn."
armorclass:
  - name: AC
    desc: "31; **Fort** +21, **Ref** +23, **Will** +19"
health:
  - name: HP
    desc: "210; explosion; **Immunities** bleed, fire, paralyzed, poison, sleep; **Weaknesses** cold 15, water 10"
abilities_mid:
  - name: "Explosion"
    desc: "When the elemental inferno dies, it explodes, dealing @Damage[7d6[fire]|options:area-damage] damage to each creature in a @Template[emanation|distance:10|traits:fire,damaging-effect] (DC 30 [[Reflex]] save)."
  - name: "Intense Heat"
    desc: "10 feet. @Damage[7d6[fire]|options:area-damage] damage DC 28 [[Reflex]] save"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tendril +24 (`pf2:1`) (reach 15 ft.), **Damage** 2d10+12 fire plus 3d8 fire"
  - name: "Ranged strike"
    desc: "Fire Mote +24 (`pf2:1`) (range 60 ft.), **Damage** 2d10+6 fire"
spellcasting: []
abilities_bot:
  - name: "Inferno Leap"
    desc: "`pf2:2` The elemental inferno jumps horizontally and vertically with a maximum height and distance each equal to its Speed. Its intense heat is suppressed until the end of the jump. Instead, at any point during the jump, flames explode from the elemental in a @Template[emanation|distance:30], dealing @Damage[12d6[fire]|options:area-damage] damage to each creature within the area (DC 30 [[Reflex]] save). <br>  <br> The elemental inferno can't Inferno Leap again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Walking conflagrations of unimaginably hot fire, elemental infernos are harbingers of destruction and heedless chaos. More tactical than many elementals, the infernos will set entire cities ablaze to confuse enemies.

Fire elementals are destructive manifestations of the scorching Plane of Fire. Although most fire elementals revel in the chance to experience new kinds of fires away from their home plane, even the most considerate fire elemental can be a danger to humanoids and their property.

```statblock
creature: "Elemental Inferno"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
