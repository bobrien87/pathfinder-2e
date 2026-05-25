---
type: creature
group: ["Fiend", "Qlippoth"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Augnagar"
level: "14"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Fiend"
trait_02: "Qlippoth"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+27; [[Darkvision]], [[Scent]] (imprecise) 30 feet, [[Truesight]] (precise) 60 feet"
languages: "Chthonian (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +27, Athletics +28, Intimidation +26"
abilityMods: ["+8", "+5", "+8", "-2", "+5", "+4"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Rotting Curse"
    desc: "**Saving Throw** DC 32 [[Fortitude]] save <br>  <br> **Stage 1** [[Drained]] 1 (1 day) <br>  <br> **Stage 2** drained 2 and the creature displays hideous, festering wounds exuding a horrific stench. When the victim takes piercing or slashing damage, creatures within 30 feet must succeed at a DC 32 [[Fortitude]] save or become [[Sickened]] 1. The victim automatically fails this save (1 day)."
armorclass:
  - name: AC
    desc: "36; **Fort** +28, **Ref** +23, **Will** +25"
health:
  - name: HP
    desc: "225; **Immunities** controlled, fear effects; **Resistances** mental 15, physical 15 except cold iron"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +28 (`pf2:1`) (magical, reach 10 ft., unarmed, unholy), **Damage** 3d12+14 piercing plus 3d6 bleed plus [[Rotting Curse]]"
  - name: "Melee strike"
    desc: "Sting +28 (`pf2:1`) (agile, finesse, magical, reach 15 ft., unholy), **Damage** 3d8+14 slashing plus 3d6 bleed"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 31, attack +23<br>**6th** [[Truesight]] (Constant)<br>**4th** [[Translocate]]"
abilities_bot:
  - name: "Confusing Display"
    desc: "`pf2:2` The augnagar's writhing limbs and flesh seethe and squirm in a disorienting and unsettling manner. Creatures in a @Template[emanation|distance:30] must attempt a DC 34 [[Will]] save, after which they are temporarily immune to further Confusing Displays for 1 minute. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Stupefied 1]] for 1 round. <br> - **Failure** The creature is stupefied 1 and [[Confused]] for 1 minute. <br> - **Critical Failure** As failure, but the creature can't attempt a flat check to recover from confusion whenever it takes damage from an attack or spell."
  - name: "Inhale Vitality"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The augnagar inhales sharply, drawing life force out of creatures in a @Template[cone|distance:50]. Creatures in the area take @Damage[14d6[void]|options:area-damage] damage with a DC 34 [[Fortitude]] save. A creature that fails its save is also [[Fatigued]]. <br>  <br> If any creatures take damage from this activity, the augnagar becomes [[Quickened]] for 1 round, and it can use the extra action only to Stride or Strike."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The brutish and gluttonous augnagar live to feast—preferably on rotten flesh and, when possible, demon flesh. But to them, the greatest delicacy is the flesh of other augnagars. Augnagars have swollen, spiderlike legs with leathery membranes like a bat's wings, and three tails ending in hooked stings perfect for slicing flesh.

An augnagar that gorges sufficiently, especially on other augnagars, can grow so massive it can't even move, thrashing and festering where it lies. It eventually flies into a frenzy of self-cannibalism as it rips apart its own flesh to feast on. From the ruinous remains emerges a thulgant—a smaller but more powerful qlippoth.

Long before the creatures known as demons came to be the dominant force in the Outer Rifts, qlippoth ruled the innumerable cracks of the Outer Sphere. These inimical creatures are a form of primordial and alien evil that predates mortal life, and most immortal life as well. Since the rise of mortal sin and the associated expansion of demonic life through the Outer Rifts, qlippoth have been driven to their deepest reaches, and they seethe with rancor at the loss of their realms. Yet, rather than directly oppose demons, qlippoth instead turn to the source—mortal sin—and wage an endless war to eradicate all creatures capable of sinful acts so that the demonic tide might be turned back. To ensure they do not bolster their foe's ranks, they enact horrific transformations on their targets, converting their victims into beings incapable of discerning right from wrong; this renders them unable to be judged by Pharasma's courts and thus incapable of becoming fiends. Most mortals consider the ministrations of a qlippoth to be far worse than any fate awaiting them in the afterlife.

```statblock
creature: "Augnagar"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
