---
type: creature
group: ["Elemental", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Filth Fire"
level: "4"
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
    desc: "+11; [[Darkvision]]"
languages: "Pyric (Can't speak any language)"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +9"
abilityMods: ["+1", "+5", "+4", "-2", "+3", "+0"]
abilities_top:
  - name: "Smoke Vision"
    desc: "The filth fire ignores the [[Concealed]] condition from smoke."
armorclass:
  - name: AC
    desc: "21; **Fort** +12, **Ref** +13, **Will** +9"
health:
  - name: HP
    desc: "70; **Immunities** bleed, fire, paralyzed, poison, sleep; **Weaknesses** cold 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Burning Lash +13 (`pf2:1`) (finesse), **Damage** 2d6+3 bludgeoning plus 1d6 fire"
  - name: "Ranged strike"
    desc: "Ember Ball +13 (`pf2:1`) (fire, range 20 ft.), **Damage** 1d6+3 bludgeoning plus 1d6 fire"
spellcasting: []
abilities_bot:
  - name: "Noxious Burst"
    desc: "`pf2:2` Toxic materials and churning rubbish within the filth fire's body explode in one of three ways. The filth fire chooses the effect, but it can't make the same choice twice in a row. <br>  <br> - **Fiery Beam** (fire, primal) The filth fire expels a @Template[type:line|distance:30] of flame that deals @Damage[3d6[fire]|options:area-damage] damage with a DC 21 [[Reflex]] save. <br> - **Shrapnel Blast** (primal) The filth fire shoots jagged rubbish out in a @Template[type:emanation|distance:5] that deals @Damage[2d12[piercing]|options:area-damage] damage with a DC 21 [[Reflex]] save. <br> - **Toxic Fumes** (poison, primal) The filth fire belches a @Template[type:cone|distance:15] of toxic smoke that deals @Damage[2d6[poison]|options:area-damage] damage (DC 21 [[Fortitude]] save). A creature that fails is also [[Sickened]] 1 ([[Sickened]] 2 on a critical failure)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These creatures look like roiling clouds of black smoke churning above a mound of burning refuse. Leering faces form and fade in the smoke above, while the burning detritus writhes in spasmodic lurches, obviously alive.

Destructive manifestations of the Plane of Fire, fire elementals sometimes incorporate burning materials into their being or superheated matter, such as molten rock or searing smoke. In combat, they tend to be aggressive and somewhat reckless. Their attacks can sometimes cause major destruction to the surrounding environment, and many fire elementals seem to enjoy seeing their flames spread far and wide.

```statblock
creature: "Filth Fire"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
