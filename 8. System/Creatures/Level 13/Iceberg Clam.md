---
type: creature
group: ["Aquatic", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Iceberg Clam"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Water"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+23; [[Darkvision]], [[Wavesense]] (imprecise) 120 feet"
languages: "Thalassic"
skills:
  - name: Skills
    desc: "Athletics +27, Nature +23, Stealth +30, Survival +25"
abilityMods: ["+6", "+5", "+8", "-2", "+4", "+3"]
abilities_top:
  - name: "Watery Body"
    desc: "The iceberg clam can occupy the same space as other creatures and is considered difficult terrain to other creatures."
armorclass:
  - name: AC
    desc: "31; **Fort** +26, **Ref** +23, **Will** +20"
health:
  - name: HP
    desc: "240; **Immunities** bleed, paralyzed, poison, sleep; **Resistances** cold 10, fire 10"
abilities_mid:
  - name: "Ambush Freeze"
    desc: "`pf2:r` **Requirements** The iceberg clam does not have a frozen shell <br>  <br> **Trigger** An enemy enters or attempts to leave the clam's space <br>  <br> **Effect** The iceberg clam uses Frozen Shell."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Freezing Wave +27 (`pf2:1`) (cold, reach 15 ft., water), **Damage** 1d12 cold plus 3d12+10 bludgeoning"
  - name: "Ranged strike"
    desc: "Icicle +26 (`pf2:1`) (cold, water, range 60 ft.), **Damage** 1d12 cold plus 3d12+4 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 30, attack +0<br>**5th** [[Wall of Ice]]<br>**4th** [[Hydraulic Torrent]], [[Ice Storm]]<br>**3rd** [[Crashing Wave]]"
abilities_bot:
  - name: "Boil"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** All creatures in the iceberg clam's space take 4d10 persistent,fire damage (DC 33 [[Fortitude]] save) and if the iceberg clam has a frozen shell, the shell takes 20 fire damage that bypasses Hardness. A creature can't recover from this persistent fire damage while in the iceberg clam's space."
  - name: "Frozen Shell"
    desc: "`pf2:1` The iceberg clam covers itself with a frozen shell. All creatures in the iceberg clam's space can't leave those squares for as long as the frozen shell is in place. The shell has AC 10, Hardness 10, and 60 Hit Points, and it's immune to critical hits and precision damage. If the iceberg clam moves, all creatures trapped within its shell move with the clam. While an iceberg clam has a frozen shell, any attacks originating from outside the iceberg clam's space must target the shell. The iceberg clam can Dismiss its shell. If the iceberg clam does so or the shell is reduced to 0 Hit Points, the iceberg clam can't use Ambush Freeze or Frozen Shell again for 1d4 rounds."
  - name: "Heated Jet"
    desc: "`pf2:2` **Requirements** The iceberg clam does not have a frozen shell <br>  <br> **Effect** The iceberg clam surges along a jet of superheated water, moving up to 60 feet in a straight line and dealing 4d10 fire damage to creatures along its path (DC 33 [[Reflex]] save)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Though technically neither an iceberg nor clam, the devastating elemental known as an iceberg clam has earned its appropriate name from its natural camouflage and feeding tendencies. This spherical ambush predator exhibits full thermal control over the water that surrounds and comprises its mutable form, luring tired swimmers and adrift vessels with the promise of reprieve before enveloping and boiling them alive.

Unless it has eaten recently enough to still be digesting its meal, a melted iceberg clam is nearly imperceptible in a large body of water. Since it's not expending energy to maintain its frozen exterior, it can wait weeks or even months before feeding again, riding ocean currents until some unlucky creature or vessel next enters its body—and never leaves.

```statblock
creature: "Iceberg Clam"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
