---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Warsworn"
level: "16"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+27; [[Darkvision]]"
languages: "Common ((Can't Speak Any Language))"
skills:
  - name: Skills
    desc: "Athletics +33"
abilityMods: ["+9", "+5", "+7", "-1", "+5", "+5"]
abilities_top:
  - name: "Animated Weapons"
    desc: "100 feet. <br>  <br> The warsworn automatically controls unattended weapons in the aura, which levitate around the warsworn. The warsworn can telekinetically wield these weapons to make melee Strikes with a reach of 100 feet. These strikes deal four of the weapon's damage dice +9 and use the weapon's damage type."
  - name: "Energy Drain"
    desc: "When a warsworn hits with a corpse wave Strike or damages a creature with Trample, the target must succeed at a DC 35 [[Fortitude]] save or become [[Drained]] 2 and [[Doomed]] 1. On a critical success, the target becomes temporarily immune to the warsworn's energy drain for 24 hours."
  - name: "Plummet"
    desc: "A creature hit by a warsworn's scrap ball Strike must attempt a DC 37 [[Reflex]] save. On a failure, the target falls [[Prone]]; if the target was airborne, it falls up to 120 feet, taking damage from the fall and landing prone if the descent brings it to the ground. On a critical failure, the target is also held under a pile of scrap (`act escape dc=37`)."
armorclass:
  - name: AC
    desc: "37; **Fort** +29, **Ref** +25, **Will** +27"
health:
  - name: HP
    desc: "350; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed"
abilities_mid:
  - name: "+1 Status to All Saves vs. Vitality"
    desc: ""
  - name: "Frightful Presence"
    desc: "100 feet. DC 35 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Absorb"
    desc: "`pf2:0` **Trigger** The warsworn moves into a dying creature's space; <br>  <br> **Effect** The warsworn absorbs the dying creature into itself, instantly killing the creature and healing the warsworn for a number of Hit Points equal to the creature's level. As long as the warsworn still exists, absorbed creatures can't be resurrected except by [[Wish]] or a similarly powerful effect."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Corpse Wave +32 (`pf2:1`) (magical), **Damage** 4d12+9 bludgeoning plus [[Energy Drain]]"
  - name: "Melee strike"
    desc: "Animated Weapon +30 (`pf2:1`) (agile, magical, reach 100 ft.), **Damage** 4d4+9 bludgeoning"
  - name: "Ranged strike"
    desc: "Scrap Ball +28 (`pf2:1`) (magical, range 100 ft.), **Damage** 4d12+9 bludgeoning plus [[Plummet]]"
spellcasting: []
abilities_bot:
  - name: "Trample"
    desc: "`pf2:3` Huge or smaller, corpse wave, DC 37 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A warsworn is an animate mass of corpses composed of dozens, sometimes even hundreds, of victims of battle. They are formed by deities of undeath or war or, rarely, spontaneously manifest from the devastation of an especially horrendous battle.

```statblock
creature: "Warsworn"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
