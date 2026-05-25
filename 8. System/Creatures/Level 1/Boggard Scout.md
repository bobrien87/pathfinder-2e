---
type: creature
group: ["Amphibious", "Boggard"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Boggard Scout"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Amphibious"
trait_02: "Boggard"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Boggard, Common"
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +8, Stealth +7"
abilityMods: ["+3", "+2", "+4", "-1", "+2", "+0"]
abilities_top:
  - name: "Swamp Passage"
    desc: "A boggard scout ignores difficult terrain caused by swamp terrain features."
  - name: "Tongue Grab"
    desc: "If the boggard scout hits a creature with their tongue, that creature becomes [[Grabbed]] by the boggard. Unlike with a normal Grab, the creature isn't [[Immobilized]], but it can't move beyond the reach of the boggard's tongue. A creature can sever the tongue by hitting AC 13 and dealing at least 2 slashing damage. Though this doesn't deal any damage to the boggard, it prevents them from using their tongue Strike until they regrow their tongue, which takes a week."
armorclass:
  - name: AC
    desc: "16; **Fort** +9, **Ref** +5, **Will** +7"
health:
  - name: HP
    desc: "24"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Morningstar +8 (`pf2:1`) (versatile p), **Damage** 1d6+3 bludgeoning"
  - name: "Melee strike"
    desc: "Tongue +8 (`pf2:1`) (reach 10 ft.), **Damage**  plus [[Tongue Grab]]"
  - name: "Ranged strike"
    desc: "Sling +7 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d6+1 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Terrifying Croak"
    desc: "`pf2:1` The boggard scout unleashes a terrifying croak. Any non-boggard within @Template[emanation|distance:30]{30 feet} becomes [[Frightened]] 1 unless they succeed at a DC 17 [[Will]] save; those who critically succeed are temporarily immune for 1 minute."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Often tasked with patrolling the borders of their lands, boggard scouts learn to speak another language (typically Common) to deal with trespassers.

Boggards are aggressive humanoid amphibians who thrive in swamps, marshes, and even some rain forests. Boggards hatch from eggs into tadpoles, fiercely competing for food and even consuming their siblings in that struggle. Over 3 years, the surviving boggards develop arms, legs, and lungs while learning the rudiments of hunting, crafts, and warfare—everything needed to survive in their might-makes-right society. At the top of most boggard hierarchies lords a hulking swampseer imbued with sinister divine magic.

```statblock
creature: "Boggard Scout"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
