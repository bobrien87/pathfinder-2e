---
type: creature
group: ["Air", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Living Thunderclap"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Air"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: "Sussuran"
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +10, Stealth +12"
abilityMods: ["+3", "+4", "+2", "-3", "+1", "+0"]
abilities_top:
  - name: "Swiftness"
    desc: "The living thunderclap doesn't trigger reactions when it moves."
armorclass:
  - name: AC
    desc: "21; **Fort** +10, **Ref** +12, **Will** +9"
health:
  - name: HP
    desc: "50; **Immunities** bleed, paralyzed, poison, sleep, sonic"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Gust +14 (`pf2:1`) (agile, finesse), **Damage** 2d6+6 bludgeoning plus [[Push]]"
  - name: "Ranged strike"
    desc: "Lightning Bolt +14 (`pf2:1`) (electricity, range 50 ft.), **Damage** 2d12 electricity"
spellcasting: []
abilities_bot:
  - name: "Thunderbolt"
    desc: "`pf2:2` The living thunderclap emits a bolt of lightning that crashes with deafening thunder. The living thunderclap makes a lightning bolt Strike that deals @Damage[1d12[electricity]|options:area-damage] damage. If it hits, the target and any creatures within a @Template[type:emanation|distance:15] around the target take @Damage[2d6[sonic]|options:area-damage] damage (DC 18 [[Fortitude]] save). Any creature that fails its save is also [[Deafened]] for 1d4 rounds."
  - name: "Push"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Push lists a distance, change the distance the creature is pushed on a success to that distance."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A living thunderclap is a small storm cloud (sometimes in the vague shape of a humanoid) that cracks and booms with thunder.

Some elementals embody aspects of air, such as smoke, lightning, and fog.

```statblock
creature: "Living Thunderclap"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
