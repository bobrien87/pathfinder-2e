---
type: creature
group: ["Dragon", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Crag Linnorm"
level: "14"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Dragon"
trait_02: "Fire"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Darkvision]], [[Scent]] (imprecise) 60 feet, [[Truesight]] (precise) 60 feet"
languages: "Aklo, Draconic, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +22, Athletics +28"
abilityMods: ["+8", "+4", "+6", "-3", "+4", "+5"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Crag Linnorm Venom"
    desc: "**Saving Throw** DC 34 [[Fortitude]] save; <br>  <br> **Maximum Duration** 10 rounds <br>  <br> **Stage 1** 4d6 fire damage and [[Drained]] 1 (1 round) <br>  <br> **Stage 2** 6d6 fire damage and [[Drained]] 2 (1 round)"
armorclass:
  - name: AC
    desc: "37; **Fort** +28, **Ref** +24, **Will** +22"
health:
  - name: HP
    desc: "270; regeneration 10 (deactivated by cold iron); **Immunities** curse, fire, paralyzed, sleep; **Weaknesses** cold iron 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 10 (Deactivated by Cold Iron)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Curse of Fire"
    desc: "When a creature slays the crag linnorm, it must succeed at a DC 35 [[Will]] save or gain weakness to fire 15 with an unlimited duration. <br>  <br> > [!danger] Effect: Curse of Fire"
  - name: "Reactive Strike (Tail Only)"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +30 (`pf2:1`) (magical, reach 20 ft., unarmed), **Damage** 3d12+14 piercing plus [[Crag Linnorm Venom]]"
  - name: "Melee strike"
    desc: "Claw +30 (`pf2:1`) (agile, magical, reach 20 ft., unarmed), **Damage** 3d8+14 slashing"
  - name: "Melee strike"
    desc: "Tail +30 (`pf2:1`) (agile, magical, reach 20 ft.), **Damage** 3d6+14 bludgeoning plus [[Improved Grab]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 33, attack +25<br>**6th** [[Truesight]] (Constant)<br>**4th** [[Unfettered Movement]] (Constant)"
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d6+14)[bludgeoning]], DC 34 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Magma Breath"
    desc: "`pf2:2` The crag linnorm breathes out a stream of magma in a @Template[line|distance:120] that deals @Damage[12d6[fire]|options:area-damage] damage to creatures within the area (DC 34 [[Reflex]] save). Any creature that fails its save also takes 4d6 persistent,fire damage. <br>  <br> The linnorm can't use Magma Breath again for 1d4 rounds. <br>  <br> The magma remains until the start of the linnorm's next turn. If the linnorm was on the ground, the magma remains as a burning line on the ground directly under the line of the Magma Breath; if the linnorm was airborne, the magma rains down in a sheet 60 feet high. Any creature that moves across or through the magma takes 6d6 fire damage (DC 34 [[Reflex]] save). <br>  <br> At the start of the linnorm's next turn, the magma cools to a thin layer of brittle stone, or the magma rain finishes falling and turns to harmless pebbles. The cooled magma quickly degrades to powder and sand over the course of several hours."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Despite being among the weakest linnorms, the crag linnorm is a devastating predator, capable of quickly cooking their foes with their magma breath.

Immense, primeval dragons of the northern reaches of the world, linnorms hate those they deem to be lesser creatures and seek to inflict as much suffering as possible upon their unfortunate victims. While these serpentine monstrosities might not be the powerful winged dragons most imagine, they nonetheless possess incredible strength and deadly powers that often rival more notorious dragons' brutality.

```statblock
creature: "Crag Linnorm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
