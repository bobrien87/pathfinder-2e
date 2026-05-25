---
type: creature
group: ["Amphibious", "Boggard"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Boggard Swampseer"
level: "3"
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
    desc: "+11; [[Darkvision]]"
languages: "Boggard, Chthonian, Common"
skills:
  - name: Skills
    desc: "Athletics +8, Intimidation +8, Medicine +9, Nature +11, Performance +8, Religion +9"
abilityMods: ["+3", "+0", "+2", "+0", "+4", "+3"]
abilities_top:
  - name: "Swamp Passage"
    desc: "A boggard swampseer ignores difficult terrain caused by swamp terrain features."
  - name: "Tongue Grab"
    desc: "If the boggard swampseer hits a creature with their tongue, that creature becomes [[Grabbed]] by the boggard. Unlike with a normal Grab, the creature isn't [[Immobilized]], but it can't move beyond the reach of the boggard's tongue. A creature can sever the tongue by hitting AC 15 and dealing at least 4 slashing damage. Though this doesn't deal any damage to the boggard, it prevents them from using their tongue Strike until they regrow their tongue, which takes a week."
armorclass:
  - name: AC
    desc: "18; **Fort** +9, **Ref** +7, **Will** +11"
health:
  - name: HP
    desc: "40"
abilities_mid:
  - name: "Drowning Drone"
    desc: "`pf2:r` **Trigger** The boggard swampseer or one of their allies within 60 feet attempts a saving throw against an auditory or sonic effect <br>  <br> **Effect** The swampseer releases a croak that drowns out other sounds. They roll a Performance check. They and boggard allies in the area can use the higher result between the swampseer's Performance check and their saves to resolve the effects against the auditory or sonic effect."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +10 (`pf2:1`) (two hand d8), **Damage** 1d4+6 bludgeoning"
  - name: "Melee strike"
    desc: "Tongue +10 (`pf2:1`) (reach 10 ft.), **Damage**  plus [[Tongue Grab]]"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 21, attack +11<br>**2nd** (2 slots) [[Acid Grip]], [[Mist]]<br>**1st** (3 slots) [[Fear]], [[Jump]], [[Runic Weapon]]<br>**Cantrips** [[Caustic Blast]], [[Frostbite]], [[Tangle Vine]]"
abilities_bot:
  - name: "Destructive Croak"
    desc: "`pf2:2` The swampseer utters a powerful croak that deals @Damage[4d6[sonic]|options:area-damage] damage to any non-boggard within a @Template[emanation|distance:15] (DC 19 [[Fortitude]] save); any creature with the [[Frightened]] condition takes additional sonic damage equal to twice the value of its frightened condition. <br>  <br> The boggard can't use Destructive Croak again for 1d4 rounds."
  - name: "Terrifying Croak"
    desc: "`pf2:1` The boggard swampseer unleashes a terrifying croak. Any non-boggard within @Template[emanation|distance:30]{30 feet} becomes [[Frightened]] 1 unless they succeed at a DC 19 [[Will]] save; those who critically succeed are temporarily immune for 1 minute."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The boggard swampseer has been gifted with magic through their worship of the demon lord Gogunta, and they use their power to rule a boggard village, keeping the rest of the village in line and planning raids on nearby communities.

Boggards are aggressive humanoid amphibians who thrive in swamps, marshes, and even some rain forests. Boggards hatch from eggs into tadpoles, fiercely competing for food and even consuming their siblings in that struggle. Over 3 years, the surviving boggards develop arms, legs, and lungs while learning the rudiments of hunting, crafts, and warfare—everything needed to survive in their might-makes-right society. At the top of most boggard hierarchies lords a hulking swampseer imbued with sinister divine magic.

```statblock
creature: "Boggard Swampseer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
