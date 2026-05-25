---
type: creature
group: ["Acid", "Amphibious"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tarn Linnorm"
level: "20"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Acid"
trait_02: "Amphibious"
trait_03: "Dragon"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+35; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Aklo, Draconic, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +32, Athletics +38, Stealth +34"
abilityMods: ["+10", "+6", "+8", "-1", "+7", "+8"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Tarn Linnorm Venom"
    desc: "**Saving Throw** DC 44 [[Fortitude]] save <br>  <br> **Maximum Duration** 10 rounds <br>  <br> **Stage 1** 7d6 acid damage and [[Drained]] 1 (1 round) <br>  <br> **Stage 2** 11d6 acid damage and [[Drained]] 2 (1 round)"
armorclass:
  - name: AC
    desc: "46 all-around vision; **Fort** +36, **Ref** +32, **Will** +31"
health:
  - name: HP
    desc: "400; regeneration 15 (deactivated by cold iron); **Immunities** acid, curse, paralyzed, sleep; **Weaknesses** cold iron 15"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 15 (Deactivated by Cold Iron)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Curse of Death"
    desc: "When a creature slays the tarn linnorm, it must succeed at a DC 46 [[Will]] save or it can no longer recover Hit Points via any means, such as healing spells, the Medicine skill, or natural healing from rest. This has an unlimited duration."
  - name: "Reactive Strike (Tail Only)"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +38 (`pf2:1`) (magical, reach 30 ft., unarmed), **Damage** 4d12+18 piercing plus [[Tarn Linnorm Venom]]"
  - name: "Melee strike"
    desc: "Claw +38 (`pf2:1`) (agile, magical, reach 30 ft., unarmed), **Damage** 4d8+18 slashing"
  - name: "Melee strike"
    desc: "Tail +38 (`pf2:1`) (agile, magical, reach 30 ft.), **Damage** 4d6+18 bludgeoning plus [[Improved Grab]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 42, attack +34<br>**6th** [[Truesight]] (Constant)<br>**4th** [[Unfettered Movement]] (Constant)"
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(3d6+18)[bludgeoning]], DC 44 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Corrosive Breath"
    desc: "`pf2:2` The tarn linnorm can expel either a @Template[line|distance:120] or a @Template[cone|distance:60] of acid, dealing @Damage[20d6[acid]|options:area-damage] damage to creatures within the area (DC 44 [[Reflex]] save). <br>  <br> The linnorm can't use Corrosive Breath or Double Breath again for 1d4 rounds. <br>  <br> The acid creates toxic fumes. At the beginning of the linnorm's next turn, those who failed the breath weapon's Reflex save must succeed at a DC 42 [[Fortitude]] save or gain [[Sickened]] 4 from the poisonous fumes."
  - name: "Double Bite"
    desc: "`pf2:1` The tarn linnorm Strides and then makes a jaws Strike with each of their heads, each against a different target. Both attacks count toward the tarn linnorm's multiple attack penalty, but the multiple attack penalty doesn't increase until after the tarn linnorm makes all of these attacks."
  - name: "Double Breath"
    desc: "`pf2:3` The tarn linnorm uses Corrosive Breath twice. A creature attempts only one save and can take damage only once. <br>  <br> The linnorm can't use Corrosive Breath or Double Breath again for 2d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Although more powerful linnorms exist, the multi-headed tarn linnorm can wreak an awe-inspiring amount of devastation.

Immense, primeval dragons of the northern reaches of the world, linnorms hate those they deem to be lesser creatures and seek to inflict as much suffering as possible upon their unfortunate victims. While these serpentine monstrosities might not be the powerful winged dragons most imagine, they nonetheless possess incredible strength and deadly powers that often rival more notorious dragons' brutality.

```statblock
creature: "Tarn Linnorm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
