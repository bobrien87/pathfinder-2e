---
type: creature
group: ["Dragon", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tor Linnorm"
level: "21"
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
    desc: "+37; [[Darkvision]], [[Scent]] (imprecise) 60 feet, [[Truesight]] (precise) 60 feet"
languages: "Aklo, Draconic, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +35, Athletics +40, Stealth +37"
abilityMods: ["+11", "+8", "+9", "-1", "+8", "+9"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Tor Linnorm Venom"
    desc: "**Saving Throw** DC 44 [[Fortitude]] save; <br>  <br> **Maximum Duration** 10 rounds <br>  <br> **Stage 1** 8d6 fire damage and [[Drained]] 1 (1 round) <br>  <br> **Stage 2** 12d6 fire damage and [[Drained]] 2 (1 round)"
armorclass:
  - name: AC
    desc: "47; **Fort** +38, **Ref** +35, **Will** +33"
health:
  - name: HP
    desc: "440; regeneration 20 (deactivated by cold iron); **Immunities** curse, fire, paralyzed, sleep; **Weaknesses** cold iron 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 20 (Deactivated by Cold Iron)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Curse of Boiling Blood"
    desc: "When a creature slays the linnorm, it must succeed at a DC 48 [[Will]] save or gain weakness to fire 20 and [[Slowed]] 1 from the agonizing pain it now endures at all times, with an unlimited duration. <br>  <br> As long as a character continues to suffer this curse, its slowed condition can never be reduced below slowed 1. <br>  <br> > [!danger] Effect: Curse of Boiling Blood"
  - name: "Lava Affinity"
    desc: "A tor linnorm can breathe and swim freely while submerged in lava and magma."
  - name: "Reactive Strike (Tail Only)"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +40 (`pf2:1`) (magical, reach 30 ft., unarmed), **Damage** 4d12+19 piercing plus [[Tor Linnorm Venom]]"
  - name: "Melee strike"
    desc: "Claw +40 (`pf2:1`) (agile, magical, reach 30 ft., unarmed), **Damage** 4d8+19 slashing"
  - name: "Melee strike"
    desc: "Tail +40 (`pf2:1`) (agile, magical, reach 30 ft.), **Damage** 4d6+19 bludgeoning plus [[Improved Grab]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 44, attack +36<br>**6th** [[Truesight]] (Constant)<br>**4th** [[Unfettered Movement]] (Constant)"
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(3d6+21)[bludgeoning]], DC 46 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Pyroclastic Breath"
    desc: "`pf2:2` The tor linnorm expels a @Template[cone|distance:60] of flame and ash dealing @Damage[20d6[fire]|options:area-damage] damage to creatures within the area (DC 46 [[Reflex]] save). <br>  <br> The linnorm can't use Pyroclastic Breath again for 1d4 rounds. <br>  <br> At the start of the tor linnorm's next turn, the area of the Pyroclastic Breath is covered in thick, scorching smoke that burns both the lungs and eyes, dealing an additional @Damage[10d6[fire]|options:area-damage] damage to all creatures in the area (DC 46 [[Reflex]] save). A creature that spends an entire round in the smoke with open eyes must succeed at a DC 44 [[Fortitude]] save or be [[Blinded]] for 1 minute. <br>  <br> The smoke dissipates after 1 minute; in strong winds, the smoke dissipates in 5 rounds, and in more powerful winds, it may clear even more quickly."
  - name: "Slashing Claws"
    desc: "`pf2:1` The tor linnorm makes four Strikes with their claws, each against a different target. These attacks count toward the tor linnorm's multiple attack penalty, but the multiple attack penalty doesn't increase until after the tor linnorm makes all their attacks."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Tor linnorms dwell in the tallest volcanic mountains, either within naturally formed caverns or molten craters. A tor linnorm's temper can be as hot and destructive as the magma the creature resembles.

Immense, primeval dragons of the northern reaches of the world, linnorms hate those they deem to be lesser creatures and seek to inflict as much suffering as possible upon their unfortunate victims. While these serpentine monstrosities might not be the powerful winged dragons most imagine, they nonetheless possess incredible strength and deadly powers that often rival more notorious dragons' brutality.

```statblock
creature: "Tor Linnorm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
