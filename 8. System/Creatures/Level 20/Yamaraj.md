---
type: creature
group: ["Monitor", "Psychopomp"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Yamaraj"
level: "20"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Monitor"
trait_02: "Psychopomp"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+37; [[Darkvision]], [[Lifesense]] (precise) 240 feet, [[Truesight]] (precise) 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian (Telepathy 120 feet, Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +33, Athletics +38, Deception +34, Diplomacy +34, Intimidation +36, Occultism +38, Religion +38, Society +38, Boneyard Lore +40, Legal Lore +40"
abilityMods: ["+10", "+7", "+7", "+10", "+7", "+6"]
abilities_top:
  - name: "Telepathy 120 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Final Judgment"
    desc: "A yamaraj's [[Manifestation]] spells are used only to pronounce judgment, typically either to restore a dead or destroyed creature to life, bind a creature to the Boneyard, or banish a creature from the Boneyard."
  - name: "Shepherd's Touch"
    desc: "A yamaraj's Strikes affect incorporeal creatures with the effects of a *[[Ghost Touch]]* property rune and deal 3d6 void damage to living creatures and 3d6 vitality damage to undead."
  - name: "Yamaraj Venom"
    desc: "While a creature is clumsy from this poison, it is [[Doomed]] with the same value; <br>  <br> **Saving Throw** DC 42 [[Fortitude]] save <br>  <br> **Maximum Duration** 10 rounds <br>  <br> **Stage 1** 3d8 poison damage and [[Clumsy]] 1 (1 round) <br>  <br> **Stage 2** 5d8 poison damage and [[Clumsy]] 2 (1 round) <br>  <br> **Stage 3** 7d8 poison damage and [[Clumsy]] 3 (1 round)"
armorclass:
  - name: AC
    desc: "45; **Fort** +33, **Ref** +31, **Will** +35"
health:
  - name: HP
    desc: "375; fast healing 20, lightning drinker; **Immunities** death effects, disease, electricity; **Resistances** void 20, poison 20"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Fast Healing 20"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Frightful Presence"
    desc: "60 feet. DC 39 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Lightning Drinker"
    desc: "Whenever a yamaraj would take electricity damage if not for its immunity, its fast healing increases to 40 on its next turn. <br>  <br> During that turn, if it uses Beetle Breath, the beetles deal 2d12 additional electricity damage."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +38 (`pf2:1`) (magical, reach 15 ft., unarmed), **Damage** 4d8+18 piercing plus [[Improved Grab]] plus [[Spirit Touch]] plus [[Yamaraj Venom]]"
  - name: "Melee strike"
    desc: "Claw +38 (`pf2:1`) (agile, magical, reach 15 ft., unarmed), **Damage** 4d4+18 slashing plus [[Spirit Touch]]"
  - name: "Melee strike"
    desc: "Tail +38 (`pf2:1`) (magical, reach 20 ft.), **Damage** 4d10+18 bludgeoning plus [[Spirit Touch]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 44, attack +36<br>**10th** [[Manifestation]], [[Revival]]<br>**9th** [[Seize Soul]], [[Wails of the Damned]]<br>**6th** [[Chain Lightning]], [[Spirit Blast]], [[Truesight]] (Constant), [[Wall of Force]]<br>**5th** [[Mind Probe (At will)]]<br>**4th** [[Translocate (At will)]]<br>**2nd** [[Dispel Magic]]<br>**1st** [[Harm]], [[Heal]]"
abilities_bot:
  - name: "Beetle Breath"
    desc: "`pf2:2` The yamaraj breathes a blast of beetles in a @Template[cone|distance:50] that deals @Damage[14d8[slashing],4d8[persistent,slashing]|options:area-damage]{14d8 slashing damage and 4d8 persistent slashing damage} to creatures in the area with a DC 42 [[Reflex]] save. <br>  <br> It can't use Beetle Breath again for 1d4 rounds. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature takes half damage and is [[Sickened]] 1. <br> - **Failure** The creature takes full damage and is [[Sickened]] 2. <br> - **Critical Failure** The creature takes double damage and is [[Sickened]] 3."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The greatest judges among the psychopomps are yamarajes, whose wisdom is legendary and whose edicts are unappealable except to ushers or Pharasma herself. A yamaraj resembles an immense dragon with dark, feathery scales and an emotionless, dispassionate gaze behind a feathered mask. When not serving as the senior magistrates, lords, and generals of the Boneyard, yamarajes pursue highly individualistic hobbies, such as gardening or literature.

Psychopomps are guardians and shepherds of the dead in the Boneyard, the vast plane of graves where mortal souls are judged and sent on to their eternal rewards or damnations. Psychopomps ensure that the dead come to terms with their transition from mortality and are properly sorted into the appropriate afterlife. They also protect souls from being preyed upon by supernatural predators. Nearly all psychopomps wear masks, especially when they're likely to be interacting with mortals, although the types of masks they wear are as varied as the psychopomps themselves. The courts of the Boneyard preside in Requian, a somber yet melodic language spoken slowly with various tonal shifts.

Many psychopomps are intimately involved with the Boneyard's massive bureaucracy. Few pursue mercy, justice, or personal gain; their duties to Pharasma and her Boneyard are supreme. Nevertheless, individual psychopomps interpret their duties in different ways, which might put them in conflict with mortals or even with each other.

```statblock
creature: "Yamaraj"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
