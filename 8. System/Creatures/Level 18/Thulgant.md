---
type: creature
group: ["Fiend", "Qlippoth"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Thulgant"
level: "18"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Fiend"
trait_02: "Qlippoth"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+30; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Chthonian (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +32, Athletics +35, Occultism +33, Stealth +32"
abilityMods: ["+9", "+6", "+6", "+5", "+6", "+9"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Thulgant Venom"
    desc: "**Saving Throw** DC 40 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 3d6 poison damage and the victim gains one of the following at random: [[Clumsy]] 1, [[Enfeebled]] 1, or [[Stupefied 1]] (1 round) <br>  <br> **Stage 2** 6d6 poison damage and the victim gains two of the following at random: [[Clumsy]] 2, [[Enfeebled]] 2, or [[Stupefied 2]] (1 round) <br>  <br> **Stage 3** 9d6 poison damage and the victim gains all three of the following: [[Clumsy]] 3, [[Enfeebled]] 3, and [[Stupefied 3]] (1 round)"
armorclass:
  - name: AC
    desc: "42; **Fort** +30, **Ref** +28, **Will** +32"
health:
  - name: HP
    desc: "305; fast healing 10; **Immunities** controlled, fear effects; **Resistances** mental 15, physical 15 except cold iron"
abilities_mid:
  - name: "Fast Healing 10"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Stinger +35 (`pf2:1`) (reach 10 ft., unholy), **Damage** 3d12+17 piercing plus 4d6 mental plus [[Thulgant Venom]]"
  - name: "Melee strike"
    desc: "Tentacle +35 (`pf2:1`) (agile, magical, reach 10 ft., unarmed, unholy), **Damage** 3d8+17 bludgeoning plus 3d6 acid plus [[Grab]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 40, attack +32<br>**8th** [[Quandary]]<br>**7th** [[Divine Decree]], [[Interplanar Teleport]]<br>**6th** [[Petrify]], [[Phantasmal Calamity]], [[Truesight]] (Constant)<br>**4th** [[Unfettered Movement]] (Constant)<br>**2nd** [[Dispel Magic]]<br>**1st** [[Daze]], [[Detect Magic]], [[Phantom Pain]]"
abilities_bot:
  - name: "Demon Hunter"
    desc: "`pf2:1` The thulgant causes a demon within 30 feet to suffer the effect of its sinful vulnerability."
  - name: "Greater Constrict"
    desc: "`pf2:1` @Damage[(2d6+17)[bludgeoning],1d6[acid]], DC 40 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC. A creature that fails this save falls [[Unconscious]], and a creature that succeeds is then temporarily immune to falling unconscious from Greater Constrict for 1 minute."
  - name: "Mind-Rending Sting"
    desc: "`pf2:1` **Requirements** The thulgant hits the same enemy with two consecutive sting Strikes in the same round <br>  <br> **Effect** The thulgant deals @Damage[(3d12+17)[mental]] damage to the enemy. If the enemy is affected by thulgant venom, that poison gains the virulent trait."
  - name: "Stunning Display"
    desc: "`pf2:2` The thulgant rises up on its twitching limbs and presents its numerous tentacles and stingers in a horrifying display of awfulness. Creatures in a @Template[emanation|distance:30] must attempt a DC 40 [[Will]] save, after which they are temporarily immune to further Stunning Displays for 1 minute. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Stunned]] 1. <br> - **Failure** The creature is [[Stunned]] 4. <br> - **Critical Failure** The creature is [[Stunned]] 8."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Thulgants are powerful and intelligent qlippoths created from the cannibalistic feeding frenzies of augnagars. Although they spend most of their time hunting and battling demons for control of the Outer Rifts, thulgants amuse themselves with a variety of diversions, such as maintaining galleries of petrified mortals or building massive, hive-like lairs filled with enslaved minions. Each thulgant is a horrific tangle of limbs, with spiderlike legs, writhing tentacles emerging from the top of its head, and three scorpion-like stingers.

Long before the creatures known as demons came to be the dominant force in the Outer Rifts, qlippoth ruled the innumerable cracks of the Outer Sphere. These inimical creatures are a form of primordial and alien evil that predates mortal life, and most immortal life as well. Since the rise of mortal sin and the associated expansion of demonic life through the Outer Rifts, qlippoth have been driven to their deepest reaches, and they seethe with rancor at the loss of their realms. Yet, rather than directly oppose demons, qlippoth instead turn to the source—mortal sin—and wage an endless war to eradicate all creatures capable of sinful acts so that the demonic tide might be turned back. To ensure they do not bolster their foe's ranks, they enact horrific transformations on their targets, converting their victims into beings incapable of discerning right from wrong; this renders them unable to be judged by Pharasma's courts and thus incapable of becoming fiends. Most mortals consider the ministrations of a qlippoth to be far worse than any fate awaiting them in the afterlife.

```statblock
creature: "Thulgant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
