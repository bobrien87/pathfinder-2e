---
type: creature
group: ["Aberration", "Titan"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hekatonkheires Titan"
level: "24"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Aberration"
trait_02: "Titan"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+43; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Aklo, Chthonian, Common, Empyrean (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +42, Athletics +48, Intimidation +45, Occultism +41, Survival +39"
abilityMods: ["+12", "+10", "+12", "+7", "+7", "+9"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "52; **Fort** +44, **Ref** +40, **Will** +37"
health:
  - name: HP
    desc: "500; **Immunities** death effects, disease"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "+4 Status to All Saves vs. Mental or Divine"
    desc: ""
  - name: "Impossible Stature"
    desc: "120 feet. Titans warp perception and distance around them to seem even larger and more imposing. A creature that enters or begins its turn within the emanation must succeed at a DC 48 [[Will]] save or its movement toward the titan is movement over difficult terrain (greater difficult terrain on a critical failure) for 1 round."
  - name: "Reactive Strike"
    desc: "`pf2:r` The hekatonkheires gains 99 extra reactions on their turn that they can use only to make Reactive Strikes. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Demolish Veil"
    desc: "`pf2:0` **Frequency** once per month <br>  <br> **Trigger** The titan casts [[Interplanar Teleport]] <br>  <br> **Effect** The titan arrives in a storm of shattered planar barriers. This has the effects of a 10th-rank [[Wrathful Storm]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Empty Weapon +45 (`pf2:1`) (magical, reach 50 ft., versatile p, versatile s), **Damage** 4d12+18 bludgeoning"
  - name: "Melee strike"
    desc: "Empty Weapon +43 (`pf2:1`) (magical, thrown 200, versatile p, versatile s), **Damage** 4d12+18 bludgeoning"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 48, attack +40<br>**9th** [[Phantasmagoria]], [[Seize Soul]]<br>**7th** [[Interplanar Teleport]]<br>**6th** [[Truesight]] (Constant)<br>**4th** [[Translocate]], [[Unfettered Movement]] (Constant)"
abilities_bot:
  - name: "Hundred-Dimension Grasp"
    desc: "`pf2:1` The titan reaches between realities to drag foes closer. They attempt an [[Athletics]] check and compare the result to the Fortitude DCs of all foes within 120 feet. On a success, a foe is teleported to any square the titan chooses within 120 feet; on a critical success, it's also [[Paralyzed]] for 1 round. The titan can [[Grab|Grab]] any foe brought within 30 feet as a free action."
  - name: "Hundred-Handed Whirlwind"
    desc: "`pf2:2` The titan overwhelms opponents with blows both conventional and interplanar. They make one empty weapon Strike against each foe within reach. Even on a failed attack (but not a critical failure), the titan deals 24 force damage to the target. This counts as three attacks for the titan's multiple attack penalty, but the penalty doesn't increase until all attacks have been made."
  - name: "Send Beyond"
    desc: "`pf2:1` **Requirements** The titan has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The titan thrusts the creature into a nightmare realm full of lightless hands and eyes. This has the effects of [[Quandary]] (DC 48). The titan can't use Send Beyond for 1d4 rounds."
  - name: "Shape Emptiness"
    desc: "`pf2:0` The titan molds a weapon from interstellar darkness. This empty weapon is a *+3 major striking weapon* in any form. The titan can't be disarmed of this weapon and it deals an additional 2d12 force damage. If Released, an *empty weapon* vanishes."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The first three hekatonkheires were meant to guard the gates to the Outer Rifts, but they proved too terrifying and rebellious—and so, in disgust, the gods cast them into the gulfs between the planes. Hekatonkheires titans are incomplete, monstrous progeny of the original three, from whom these titans calved like icebergs. Hekatonkheires wield interstellar darkness as a weapon and spurn the limits of physical reality, literally reaching through space with their countless arms. Filled with a drive to either discover their lost identity or create a new one, they metaphysically disembowel ancient beings and cosmic magics, using the entrails to find clues regarding their own nature and parentage or to serve as raw materials for fueling some alien apotheosis.

Created by ancient deities long before the rise of mortal ancestries, titans united and attempted to overthrow their deific progenitors. The resulting war still figures prominently throughout mortal myths, in which most titans were cast down and imprisoned for eons.

```statblock
creature: "Hekatonkheires Titan"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
