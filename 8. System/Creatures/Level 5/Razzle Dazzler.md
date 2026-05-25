---
type: creature
group: ["Gnome", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Razzle Dazzler"
level: "5"
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
    desc: "+12; [[Low-Light Vision]]"
languages: "Common, Elven, Fey, Gnomish"
skills:
  - name: Skills
    desc: "Arcana +10, Deception +14, Diplomacy +14, Intimidation +12, Performance +14, Thievery +12"
abilityMods: ["+1", "+3", "+1", "+2", "+1", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20; **Fort** +9, **Ref** +12, **Will** +15"
health:
  - name: HP
    desc: "78"
abilities_mid:
  - name: "Daunting Charisma"
    desc: "`pf2:0` **Trigger** The razzle dazzler rolls initiative using Deception or Performance <br>  <br> **Effect** The razzle dazzler can attempt to `act demoralize` one creature they can see."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +13 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+3 piercing"
  - name: "Melee strike"
    desc: "Dagger +13 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+3 piercing"
  - name: "Melee strike"
    desc: "Fist +13 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +13 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6+2 piercing"
spellcasting:
  - name: "Arcane Spontaneous Spells"
    desc: "DC 22, attack +15<br>**3rd** (3 slots) [[Enthrall]], [[Hypnotize]]<br>**2nd** (4 slots) [[Illusory Creature]], [[Laughing Fit]], [[Revealing Light]]<br>**1st** (4 slots) [[Dizzying Colors]], [[Figment]], [[Illusory Disguise]], [[Illusory Disguise]], [[Illusory Object]], [[Illusory Object]], [[Light]], [[Prestidigitation]], [[Telekinetic Hand]], [[Telekinetic Projectile]], [[Ventriloquism]]"
abilities_bot:
  - name: "Dazzling Duplicate"
    desc: "`pf2:1` The razzle dazzler creates an illusory duplicate of themself in their space that lasts for 1 round. A creature who attacks the razzle dazzler must first attempt a DC 11 flat check. On a failure, the attack misses the razzle dazzler and destroys the illusion instead, ending this effect."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The razzle dazzler is a particularly beguiling sort of entertainer who specializes in delighting with illusions and showy displays. Whether with their illusory double or some well-timed fireworks, they are exceptionally good at keeping their audiences focused on one display to distract from the secrets that make their magic possible.

Because their ancestors came from the First World, gnomes are intrinsically linked to the realm of the fey and crave the mystical and unpredictable. They seek to create daring works of art, voyage to new places, and have experiences they've never had before. Otherwise, they could fall victim to the terrible gnomish illness known as the Bleaching, which not only drains them of their color but of their spirits as well.

```statblock
creature: "Razzle Dazzler"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
