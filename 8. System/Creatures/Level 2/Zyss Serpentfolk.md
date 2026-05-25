---
type: creature
group: ["Humanoid", "Serpentfolk"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Zyss Serpentfolk"
level: "2"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Serpentfolk"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Aklo, Common, Sakvroth (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +8, Arcana +8, Deception +9, Occultism +8, Society +8"
abilityMods: ["-1", "+4", "-2", "+4", "+2", "+3"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Serpentfolk Venom"
    desc: "**Saving Throw** DC 16 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 2d4 poison damage and enfeebled 1 (1 round)"
armorclass:
  - name: AC
    desc: "18; **Fort** +4, **Ref** +8, **Will** +8 ; +1 status to all saves vs. magic"
health:
  - name: HP
    desc: "25; **Resistances** poison 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "+4 Status to Will Saves vs. Mental"
    desc: ""
  - name: "Thin of Blood"
    desc: "Zyss serpentfolk recover slowly from injuries. When they take physical damage from a critical hit, they gain 1d4 persistent,bleed damage. They take a –2 circumstance penalty to flat checks to recover from persistent damage and saving throws against afflictions."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +10 (`pf2:1`) (finesse), **Damage** 1d6+1 piercing plus [[Serpentfolk Venom]]"
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+1 piercing plus [[Serpentfolk Venom]]"
  - name: "Ranged strike"
    desc: "Shortbow +10 (`pf2:1`) (deadly d10, range 60 ft.), **Damage** 1d6+2 piercing plus [[Serpentfolk Venom]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 18, attack +10<br>**4th** [[Suggestion]]<br>**2nd** [[Blur (Self Only, At Will)]]<br>**1st** [[Illusory Disguise]] (At Will), [[Ventriloquism]] (At Will)"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Even the least among zyss serpentfolk consider themselves greater than any mammal. Their magical abilities, most notably their telepathy, are all the reason they need to hold this view. And it's true enough that the instinctual skill and magic of any zyss is enough to best the average human.

Before their ancient clash with humanity devastated their civilization, serpentfolk were masters of a sprawling underground empire. Their power was shattered and their god Ydersius decapitated (although not quite slain). The cunning, intelligence, and magical abilities of serpentfolk have diminished from their ancient heights, and most are born without these boons. This is partially the result of cruel genetic meddling among serpentfolk—though the ruling class, zyss, are born with an innate spellcasting ability, their blood runs thin, making them susceptible to wounds. Seen as the failures of the serpentfolk's experiments are the aapophs, who are strong but prone to mutation and lack innate spellcasting.

Today, the central realm of the Darklands retains the old name of the serpentfolk empire that once dominated this region—Sekamina. This name is also the source of the serpentfolk's Aklo title, sekmin, which they are often called in ancient texts. Serpentfolk dominion had declined before ghouls, gugs, umbral gnomes, and other forces. Yet their recent ventures have brought them back to a stronger place in the Darklands. Many serpentfolk sleeping in torpor in secluded vaults have awakened.

Zyss serpentfolk tend toward megalomania, with dreams of returning to their place of dominance. Many of their plans hinge on resurrecting Ydersius, their decapitated god. His headless body still thrashes about, mindless, in the Darklands, waiting to be reunited with his lost skull. Serpentfolk numbers are so small that reclaiming their dominance seems a distant dream, especially since their reproduction is slow. Though a parent can birth a dozen young at once, the gestation period lasts up to a decade, and the likelihood that even one will be zyss is low. There's no telling whether a child will be zyss or aapoph, regardless of parentage. A coveted zyss child is just as likely to arise from aapoph parents as from two zyss, and every serpentfolk colony has someone in charge of sorting the young, identifying the earliest signs of magic in them.

```statblock
creature: "Zyss Serpentfolk"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
