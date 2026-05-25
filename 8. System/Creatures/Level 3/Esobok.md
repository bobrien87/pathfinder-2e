---
type: creature
group: ["Monitor", "Psychopomp"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Esobok"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Monitor"
trait_02: "Psychopomp"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]], [[Lifesense]] (imprecise) 60 feet, [[Scent]] (imprecise) 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +8, Intimidation +9, Religion +4, Stealth +8, Survival +10"
abilityMods: ["+3", "+3", "+4", "-3", "+3", "+2"]
abilities_top:
  - name: "Shepherd's Touch"
    desc: "An esobok's Strikes affect incorporeal creatures with the effects of a *[[Ghost Touch]]* property rune and deal 1d6 void damage to living creatures and 1d6 vitality damage to undead."
armorclass:
  - name: AC
    desc: "18; **Fort** +11, **Ref** +8, **Will** +8"
health:
  - name: HP
    desc: "55; **Immunities** death effects, disease; **Resistances** poison 5, void 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +12 (`pf2:1`) (magical), **Damage** 1d10+3 piercing plus [[Grab]] plus [[Spirit Touch]]"
  - name: "Melee strike"
    desc: "Claw +12 (`pf2:1`) (agile, magical), **Damage** 1d6+3 slashing plus [[Spirit Touch]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 0, attack +0<br>**2nd** [[Invisibility (Self Only)]]"
abilities_bot:
  - name: "Pounce"
    desc: "`pf2:1` The esobok Strides and then makes a Strike. If it began this action [[Hidden]], it remains hidden until after the Strike."
  - name: "Wrench Spirit"
    desc: "`pf2:1` **Requirements** A creature is [[Grabbed]] or [[Restrained]] by the esobok's jaws <br>  <br> **Effect** The esobok releases the target from the Grab but wrenches its spirit free as it does so. The creature must attempt a DC 20 [[Will]] save. Creatures without souls (such as most constructs) and creatures whose bodies and souls are one (such as most celestials, fiends, and monitors) who roll a failure or critical failure on the save get a success instead. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The target is [[Stunned]] 1. <br> - **Failure** The esobok wrenches the target's soul from its body into its jaws. Mindless undead creatures of level 2 or lower are destroyed, other undead creatures are stunned for 1 round, and all other creatures are [[Paralyzed]]. At the end of each of its turns, a creature paralyzed by this effect can attempt a new save to end the effect. The paralysis ends automatically if the esobok attempts a jaws Strike or speaks."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Esoboks are brute hunters and pugnacious sentinels who serve as the guard dogs of the Boneyard. These squat, powerful quadrupeds have a frill of dark feathers around their distinctive heads which resemble a crocodile skull. Esoboks rarely bother with those who are truly dead, allowing the dead of the Boneyard to go about their business while remaining watchful for danger. Though cunning when sniffing out threats to the Boneyard or to their psychopomp handlers, they're among the least intelligent of the psychopomps and rarely speak except to utter growling threats. The wise listen when an esobok makes a threat, as it won't do so twice.

Many psychopomps are intimately involved with the Boneyard's massive bureaucracy. Few pursue mercy, justice, or personal gain; their duties to Pharasma and her Boneyard are supreme. Nevertheless, individual psychopomps interpret their duties in different ways, which might put them in conflict with mortals or even with each other.

```statblock
creature: "Esobok"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
