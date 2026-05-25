---
type: creature
group: ["Aiuvarin", "Elf"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Aiuvarin Elementalist"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aiuvarin"
trait_02: "Elf"
trait_03: "Human"
trait_04: "Humanoid"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Low-Light Vision]]"
languages: "Common, Elven"
skills:
  - name: Skills
    desc: "Acrobatics +7, Arcana +8, Athletics +5, Deception +4, Nature +6, Stealth +7, Elemental Lore +8"
abilityMods: ["+0", "+0", "+0", "+0", "+0", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +5, **Ref** +11, **Will** +8"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+3 piercing"
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+3 piercing"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 18, attack +10<br>**1st** (4 slots) [[Gentle Landing]], [[Gust of Wind]], [[Illusory Disguise]], [[Thunderstrike]]<br>**Cantrips** [[Detect Magic]], [[Electric Arc]], [[Light]], [[Message]], [[Shield]]"
abilities_bot:
  - name: "Elemental Field"
    desc: "`pf2:2` The elementalist unleashes powerful static electricity in a @Template[emanation|distance:20] that lasts for 1 minute. All squares in the area become hazardous terrain for other creatures. A creature takes @Damage[1[electricity]|options:area-damage] damage each time it moves into one of these squares. While in the area, creatures take a –1 status penalty to saves against electricity spells. <br>  <br> > [!danger] Effect: Elemental Field"
  - name: "Elf Step"
    desc: "`pf2:1` The elementalist Steps twice."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Commonly referred to as half-elves, aiuvarins often have trouble fitting into society. This can lead to many aiuvarins diverting their full attention towards their own personal pursuits, such as studying spellcasting.

Elves are mysterious and intelligent, and graceful and cunning in battle.

```statblock
creature: "Aiuvarin Elementalist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
