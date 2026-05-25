---
type: creature
group: ["Air", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Elemental Hurricane"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Air"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]]"
languages: "Sussuran"
skills:
  - name: Skills
    desc: "Acrobatics +24, Athletics +21, Stealth +22"
abilityMods: ["+6", "+7", "+4", "+0", "+3", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "32; **Fort** +19, **Ref** +24, **Will** +18"
health:
  - name: HP
    desc: "140; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Disperse"
    desc: "`pf2:r` **Trigger** The elemental hurricane takes damage from a hostile action. <br>  <br> **Effect** The elemental hurricane disperses. <br>  <br> Until the end of the current turn, it can't be attacked or targeted, doesn't take up space, and any auras or emanations it has are suppressed. At the end of the turn, the elemental hurricane reforms in any space in which it can fit within 100 feet of where it dispersed and any auras or emanations it has are restored as long as their duration didn't run out while it was dispersed."
  - name: "High Winds"
    desc: "40 feet. <br>  <br> Air within the emanation is difficult terrain for Flying creatures that don't have the air trait."
  - name: "Swiftness"
    desc: "The elemental's movement doesn't trigger reactions."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Gust +24 (`pf2:1`) (finesse, reach 20 ft.), **Damage** 2d10+12 bludgeoning plus [[Push]]"
  - name: "Ranged strike"
    desc: "Lightning Lash +24 (`pf2:1`) (range 75 ft.), **Damage** 2d12+6 electricity"
spellcasting: []
abilities_bot:
  - name: "Gale Breath"
    desc: "`pf2:2` The elemental exhales a @Template[cone|distance:30] of air. Creatures in the cone must succeed at a DC 29 [[Fortitude]] save or be knocked away from the elemental. <br>  <br> A creature knocked into a solid object stops moving and takes @Damage[10d6[bludgeoning]|options:area-damage] damage (roll the damage once for all creatures). <br>  <br> The elemental hurricane can't use Gale Breath again for 1d4 rounds. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is pushed 20 feet. <br> - **Failure** The creature is pushed 40 feet. <br> - **Critical Failure** The creature is pushed 40 feet and knocked [[Prone]]."
  - name: "Push 10 feet"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Push lists a distance, change the distance the creature is pushed on a success to that distance."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Elemental hurricanes embody the ferocity of violent windstorms.

Hailing from the Plane of Air, these beings appear in a variety of sizes and shapes. They're noted for being elusive, swift, and often difficult to detect due to being composed primarily of air.

```statblock
creature: "Elemental Hurricane"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
