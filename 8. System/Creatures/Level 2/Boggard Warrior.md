---
type: creature
group: ["Amphibious", "Boggard"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Boggard Warrior"
level: "2"
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
    desc: "+8; [[Darkvision]]"
languages: "Boggard"
skills:
  - name: Skills
    desc: "Athletics +8, Intimidation +5, Stealth +6"
abilityMods: ["+4", "+0", "+4", "-1", "+2", "+1"]
abilities_top:
  - name: "Swamp Passage"
    desc: "A boggard warrior ignores difficult terrain caused by swamp terrain features."
  - name: "Tongue Grab"
    desc: "If the boggard warrior hits a creature with their tongue, that creature becomes [[Grabbed]] by the boggard. Unlike with a normal Grab, the creature isn't [[Immobilized]], but it can't move beyond the reach of the boggard's tongue. A creature can sever the tongue by hitting AC 15 and dealing at least 3 slashing damage. Though this doesn't deal any damage to the boggard, it prevents them from using their tongue Strike until they regrow their tongue, which takes a week."
armorclass:
  - name: AC
    desc: "17; **Fort** +10, **Ref** +5, **Will** +8"
health:
  - name: HP
    desc: "38"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Club +10 (`pf2:1`), **Damage** 1d6+6 bludgeoning"
  - name: "Melee strike"
    desc: "Tongue +10 (`pf2:1`) (reach 10 ft.), **Damage**  plus [[Tongue Grab]]"
  - name: "Melee strike"
    desc: "Javelin +6 (`pf2:1`) (thrown 30), **Damage** 1d6+4 piercing"
  - name: "Melee strike"
    desc: "Club +6 (`pf2:1`) (thrown 10), **Damage** 1d6+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Terrifying Croak"
    desc: "`pf2:1` The boggard warrior unleashes a terrifying croak. Any non-boggard within @Template[emanation|distance:30]{30 feet} becomes [[Frightened]] 1 unless they succeed at a DC 18 [[Will]] save; those who critically succeed are temporarily immune for 1 minute."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Boggard warriors exalt single combat and prefer to fight alone so that no one can contest their kills. They have been known to pursue enemies who flee combat with a single-mindedness that seems almost supernatural.

Boggards are aggressive humanoid amphibians who thrive in swamps, marshes, and even some rain forests. Boggards hatch from eggs into tadpoles, fiercely competing for food and even consuming their siblings in that struggle. Over 3 years, the surviving boggards develop arms, legs, and lungs while learning the rudiments of hunting, crafts, and warfare—everything needed to survive in their might-makes-right society. At the top of most boggard hierarchies lords a hulking swampseer imbued with sinister divine magic.

```statblock
creature: "Boggard Warrior"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
