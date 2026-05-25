---
type: creature
group: ["Earth", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Earthen Destrier"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]], [[Tremorsense]] (imprecise) 60 feet"
languages: "Petran"
skills:
  - name: Skills
    desc: "Athletics +12"
abilityMods: ["+4", "+1", "+4", "-1", "+3", "+0"]
abilities_top:
  - name: "Earth Glide"
    desc: "An earthen destrier can [[Burrow]] through earthen matter, including rock. When it does so, it moves at its full burrow Speed, leaving no tunnels or signs of its passing."
  - name: "Lancing Charge"
    desc: "If the destrier moved at least 10 feet directly before its lance arm Strike, it gains a +2 circumstance bonus to its damage roll."
armorclass:
  - name: AC
    desc: "20; **Fort** +14, **Ref** +9, **Will** +10"
health:
  - name: HP
    desc: "75; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Tilting Strike"
    desc: "`pf2:r` **Trigger** The earthen destrier tramples a creature <br>  <br> **Effect** The earthen destrier makes a lance arm Strike against the creature it's Trampling with a –5 circumstance penalty."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Lance Arm +14 (`pf2:1`) (deadly d8, reach 10 ft.), **Damage** 2d8+6 piercing plus [[Lancing Charge]]"
  - name: "Melee strike"
    desc: "Hoof +14 (`pf2:1`), **Damage** 2d6+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Trample"
    desc: "`pf2:3` Medium or smaller, hoof, DC 20 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

This wave of dirt takes the crude likeness of the melded forequarters of a charging warhorse and a rocky knight wielding a rudimentary lance of gray stone.

Certain earth elementals manifest as specific types of material, be they boulders, sand, or crystals.

```statblock
creature: "Earthen Destrier"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
