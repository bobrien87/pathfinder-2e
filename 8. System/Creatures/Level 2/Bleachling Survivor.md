---
type: creature
group: ["Gnome", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bleachling Survivor"
level: "2"
rare_01: "Uncommon"
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
    desc: "+8; [[Low-Light Vision]]"
languages: "Common, Fey, Gnomish"
skills:
  - name: Skills
    desc: "Intimidation +7, Medicine +8, Occultism +7, Survival +8"
abilityMods: ["+1", "+1", "+3", "+1", "+3", "+1"]
abilities_top:
  - name: "Unflappable"
    desc: "When the bleachling survivor rolls a critical failure on a check with the emotion trait, they get a failure instead."
  - name: "Sneak Attack"
    desc: "The bleachling survivor deals an extra 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "17; **Fort** +5, **Ref** +8, **Will** +12"
health:
  - name: HP
    desc: "34"
abilities_mid:
  - name: "Flinch Back"
    desc: "`pf2:r` **Trigger** An enemy moves into an adjacent space <br>  <br> **Effect** The bleachling survivor Steps up to 10 feet. They must end this movement in a space that is not adjacent to an enemy."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, finesse, thrown 10, versatile s), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+1 bludgeoning"
  - name: "Ranged strike"
    desc: "Longbow +9 (`pf2:1`) (deadly d10, reload 0, volley 30, range 100 ft.), **Damage** 1d8 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

It is almost unheard of for gnomes to survive the horrendous sickness known as the Bleaching, but those few who do are permanently altered. Having lived through the worst disease known to their kind, bleachling survivors often emerge jaded and reckless, traveling to seek out mind-bending experiences and heady thrills that will awaken something in them again. Though their experiences may toughen them, they are not unfriendly. Most try to help others they meet during their travels who might not be as unshakable.

Because their ancestors came from the First World, gnomes are intrinsically linked to the realm of the fey and crave the mystical and unpredictable. They seek to create daring works of art, voyage to new places, and have experiences they've never had before. Otherwise, they could fall victim to the terrible gnomish illness known as the Bleaching, which not only drains them of their color but of their spirits as well.

```statblock
creature: "Bleachling Survivor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
