---
type: creature
group: ["Fey", "Sprite"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Draxie"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fey"
trait_02: "Sprite"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Low-Light Vision]]"
languages: "Common, Fey (Telepathy (Touch))"
skills:
  - name: Skills
    desc: "Acrobatics +9, Deception +10, Diplomacy +8, Nature +6, Stealth +11"
abilityMods: ["-1", "+4", "+1", "+3", "+1", "+3"]
abilities_top:
  - name: "Telepathy (Touch)"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "19; **Fort** +6, **Ref** +11, **Will** +8"
health:
  - name: HP
    desc: "45; **Weaknesses** cold iron 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +11 (`pf2:1`) (agile, finesse, magical, unarmed), **Damage** 1d8+3 bludgeoning"
  - name: "Ranged strike"
    desc: "Euphoric Spark +7 (`pf2:1`) (magical), **Damage** 2d4+3 mental"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 20, attack +12<br>**2nd** [[Invisibility]], [[Revealing Light]]<br>**1st** [[Figment]], [[Illusory Disguise]], [[Light]], [[Prestidigitation]]"
abilities_bot:
  - name: "Draxie Dust"
    desc: "`pf2:2` The draxie breathes magical dust in a @Template[cone|distance:15]. Roll `r 1d4` to determine the effect. Each creature in the area must succeed at a DC 17 [[Will]] save or be affected. <br>  <br> The draxie can't use Draxie Dust again for 1d4 rounds. <br>  <br> - The target takes the effects of the [[Charm]] spell. <br>  <br> - The target loses its last 5 minutes of memory.  <br>  <br> - The target takes the effects of a [[Sleep]] spell.  <br>  <br> - For 1 minute, the target is in a state of euphoria that makes it [[Stupefied 2]] and [[Slowed]] 1."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The mischievous dragon sprites called draxies have dueled their pixie cousins for the title of ultimate prankster for centuries. They exercise patience and planning to create the perfect pranks, spending months, or even years, on their efforts. One exception to their flighty nature is the elucrea, a lifelong bond between a draxie and a creature they're particularly fond of, typically one with a good sense of humor. According to draxie legend, a little piece of a draxie's spirit remembers being united as the ancient fey dragonet Elucredassa, and that causes draxies to yearn for such connections with others.

Elusive, flighty, and ebullient, sprites are what many villagers first imagine when they hear the terms "fey" or "fairy." While their dispositions vary, all sprites share a connection to magic and a diminutive size. This family of fey shares its name with its slightest and most populous member, the common sprite.

```statblock
creature: "Draxie"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
