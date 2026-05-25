---
type: creature
group: ["Gnome", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gnome Daredevil"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Gnome"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Low-Light Vision]]"
languages: "Common, Gnomish"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +7, Performance +8, Thievery +7"
abilityMods: ["+3", "+4", "+1", "+1", "+1", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +12, **Will** +5"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Gnome Flickmace +11 (`pf2:1`) (reach, sweep), **Damage** 1d6+3 bludgeoning plus [[Knockdown]]"
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Shortbow +9 (`pf2:1`) (deadly d10, propulsive, reload 0, range 60 ft.), **Damage** 1d6+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Daredevil Strike"
    desc: "`pf2:2` **Frequency** once per round <br>  <br> **Effect** The gnome daredevil Strides up to their Speed, makes a melee Strike, then Steps."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

These nimble warriors capitalize on their slight stature and dexterous movements to evade and overtake their foes on the battlefield. Their unmatched skill with the gnome flickmace allows a daredevil to strike from a short distance and twirl away unscathed, sometimes hitting hard enough to topple their foes.

Because their ancestors came from the First World, gnomes are intrinsically linked to the realm of the fey and crave the mystical and unpredictable. They seek to create daring works of art, voyage to new places, and have experiences they've never had before. Otherwise, they could fall victim to the terrible gnomish illness known as the Bleaching, which not only drains them of their color but of their spirits as well.

```statblock
creature: "Gnome Daredevil"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
