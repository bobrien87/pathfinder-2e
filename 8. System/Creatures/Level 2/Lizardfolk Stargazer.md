---
type: creature
group: ["Humanoid", "Lizardfolk"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lizardfolk Stargazer"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Lizardfolk"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8"
languages: "Draconic, Iruxi, Common"
skills:
  - name: Skills
    desc: "Diplomacy +4, Nature +8, Stealth +6, Survival +8, Iruxi Lore +6"
abilityMods: ["+2", "+2", "+1", "+0", "+4", "+0"]
abilities_top:
  - name: "Deep Breath"
    desc: "A lizardfolk stargazer can hold their breath for 20 minutes."
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +6, **Will** +10"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +8 (`pf2:1`) (two hand d8), **Damage** 1d6+2 bludgeoning"
  - name: "Melee strike"
    desc: "Jaws +8 (`pf2:1`) (unarmed), **Damage** 1d6+2 piercing"
  - name: "Melee strike"
    desc: "Tail +8 (`pf2:1`) (agile, finesse), **Damage** 1d4+2 bludgeoning"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 18, attack +10<br>**1st** (5 slots) [[Charm]], [[Heal]], [[Runic Body]], [[Pest Form]], [[Summon Animal]]<br>**Cantrips** [[Guidance]], [[Ignition]], [[Know the Way]], [[Light]], [[Stabilize]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The tradition of astrology and looking to the stars for both navigation and prognostication is well-established in iruxi society, and their wise and observant stargazers are among the people's most respected members. Even the lowliest stargazer, as presented here, has a number of useful primal spells to aid their kin; in larger iruxi settlements, stargazers wield even greater powers.

Capable and adaptable predators, the reptilian beings known as lizardfolk are heirs to truly ancient civilizations. Their oral traditions cover thousands of years, and they revere the bones of their ancestors. Fossilized lizardfolk are even built into the walls of lizardfolk's stone and glass cities, to allow these predecessors to watch over their kin. Lizardfolk likewise have longstanding traditions of religious worship and astrology, with eyes on the past, the future, and the stars whenever they make a large decision. Their long history has taught them to be patient in all things, though this has seen them losing ground to hastier peoples in modern times.

Lizardfolk refer to themselves as "iruxi," though they have taken their common moniker among other peoples in stride. Most of their settlements are entirely communal, with hatchlings raised by anyone with the time and temperament for such a role. Iruxis dwell and thrive in all tropical and temperate biomes, but they are most at home in swamplands, coastal regions, and river lands. They are talented swimmers, and many of their major cities are partially submerged to take advantage of this fact, causing them to often be overlooked by others. Fish and aquatic plants make up a large part of their preferred diets.

```statblock
creature: "Lizardfolk Stargazer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
