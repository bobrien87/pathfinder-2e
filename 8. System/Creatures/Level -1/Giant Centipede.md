---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Centipede"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +2, Stealth +6"
abilityMods: ["-1", "+3", "+1", "-5", "+1", "-4"]
abilities_top:
  - name: "Giant Centipede Venom"
    desc: "**Saving Throw** DC 14 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage (1 round) <br>  <br> **Stage 2** 1d4 poison damage and [[Off Guard]] (1 round) <br>  <br> **Stage 3** 1d4 poison damage, [[Clumsy]] 1, and [[Fatigued]] (1 round)"
armorclass:
  - name: AC
    desc: "15; **Fort** +7, **Ref** +6, **Will** +2"
health:
  - name: HP
    desc: "8"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandibles +6 (`pf2:1`) (finesse), **Damage** 1d4-1 piercing plus [[Giant Centipede Venom]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Most giant centipedes (known as sewer centipedes when found in cities) nest in small groups but hunt alone when they seek out food. Attempts to domesticate giant centipedes for use as guardians or pets generally end poorly, but some communities of goblins, kobolds, and mitflits have developed effective methods of utilizing these vermin as guardians. Other groups roast and eat centipedes, often with pungent peppers as a savory delicacy, although care must be taken in preparing the meal to avoid tainting the flesh with the creature's venom.

Hunters and scavengers that live amid dung and detritus, centipedes are a relatively common and often reviled threat faced by adventurers. Scurrying about with surprising speed on the scores of legs attached to their long, segmented bodies, centipedes strike with poisoned mandibles to slow and torment their prey with a vicious toxin before they settle down to feed in slow and disgusting leisure.

```statblock
creature: "Giant Centipede"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
