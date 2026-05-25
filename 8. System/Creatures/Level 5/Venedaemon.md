---
type: creature
group: ["Daemon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Venedaemon"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: "Aklo, Chthonian, Common, Daemonic, Diabolic, Draconic, Requian (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +13, Arcana +16, Deception +12, Occultism +14, Religion +13, Scribing Lore +14"
abilityMods: ["+2", "+4", "+2", "+5", "+3", "+3"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Smell Magic (Imprecise) 60 feet"
    desc: "A venedaemon is aware of magical items and active spells as an imprecise sense. The subtle differences in these scents reveal the tradition and traits of the magic."
  - name: "Soul Spell"
    desc: "If a venedaemon ingest a soul gem from a cacodaemon, they can recover an expended spell slot instead of gaining fast healing. The spell slot's rank can be no higher than half the level of the creature whose soul was consumed, rounded up."
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +11, **Will** +14"
health:
  - name: HP
    desc: "75; **Immunities** death effects; **Weaknesses** holy 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tentacle +13 (`pf2:1`) (agile, finesse, magical, reach 10 ft., unarmed, unholy), **Damage** 2d6+5 bludgeoning"
spellcasting:
  - name: "Arcane Spontaneous Spells"
    desc: "DC 22, attack +14<br>**3rd** (3 slots) [[Fireball]], [[Levitate]], [[Paralyze]]<br>**2nd** (4 slots) [[Blazing Bolt]], [[Dispel Magic]], [[Invisibility]], [[Noise Blast]]<br>**1st** (4 slots) [[Electric Arc]], [[Enfeeble]], [[Fear]], [[Force Barrage]], [[Illusory Disguise]], [[Shield]], [[Sigil]], [[Telekinetic Hand]], [[Void Warp]]"
  - name: "Divine Innate Spells"
    desc: "DC 22, attack +14<br>**4th** [[Translocate]]"
abilities_bot:
  - name: "Residual Force"
    desc: "`pf2:1` **Requirements** The venedaemon's most recent action was to cast a spell <br>  <br> **Effect** Fading runes cling to the venedaemon's tentacles. The venedaemon makes a tentacle Strike that has a reach of 20 feet and deals 2d4 additional force damage."
  - name: "Twisted Whispers"
    desc: "`pf2:1` The venedaemon whispers to a creature within 15 feet, which must succeed at a DC 22 [[Will]] save or be [[Stupefied 2]] for 1 minute (or [[Stupefied 3]] on a critical failure). <br>  <br> Regardless of the results of the save, the creature is immune to Twisted Whispers for 24 hours."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Those killed by magic or killed in the pursuit of magic can arise as venedaemons. Although among the weaker daemons, these robed figures can often be seen serving as researchers or clerks throughout the plane. Even within the mortal Universe, scholars barter souls or arcane knowledge with venedaemons for their secrets and assistance.

Denizens of the bleak and terrible plane of Abaddon, daemons are shaped by and devoted to the destruction of life in all its forms. They seek the death of every mortal being by the most painful and horrible means possible, in service to the Apocalypse Riders. Each kind of daemon represents a different way to die, and their powers are nearly always aimed at spreading that particular form of death. Through the use of these powers, they seek to drag all existence down into a pit of hopelessness and despair, and to commit all souls to oblivion.

While mortals who summon daemons usually seek to use the creatures' destructive and corrupting powers for their own ends, daemons always look for ways to spread fear, doubt, and despair wherever they go. Often, daemons disguise their plots as the workings of other fiends, knowing that such confusion compounds mortals' fear and keeps those mortals from bringing the most effective weapons. As a result, learned mortals sometimes refer to daemons as "riders" after their leaders or "soul mongers" after their largest industry.

While many fiends seek to tempt mortals into lives of nihilistic evil to increase their own numbers and power on their native planes, daemons are further driven by a supernatural hunger for mortal souls and use a variety of methods—not least of which is the cacodaemons' soul gems—to entrap them. On Abaddon and in other forbidding places across the multiverse, souls are simultaneously a delicacy, a trade good, and a source of magical power, and the daemons are among the greatest gluttons, merchants, and abusers of this spiritual "resource."

```statblock
creature: "Venedaemon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
