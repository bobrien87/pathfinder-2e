---
type: creature
group: ["Dragon", "Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fey Dragonet"
level: "2"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Dragon"
trait_02: "Fey"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Common, Draconic, Fey (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +8, Deception +8, Diplomacy +8, Nature +4, Stealth +10"
abilityMods: ["-2", "+4", "+0", "+2", "+0", "+2"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "18; **Fort** +5, **Ref** +12, **Will** +11"
health:
  - name: HP
    desc: "30; **Immunities** paralyzed, sleep"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`) (finesse, magical, unarmed), **Damage** 1d4 piercing"
spellcasting:
  - name: "Arcane Spontaneous Spells"
    desc: "DC 18, attack +10<br>**1st** (4 slots) [[Figment]], [[Grease]], [[Illusory Object]], [[Light]], [[Prestidigitation]], [[Sleep]], [[Tangle Vine]], [[Telekinetic Projectile]]"
  - name: "Arcane Innate Spells"
    desc: "DC 21, attack +13<br>**2nd** [[Invisibility (Self Only)]]"
abilities_bot:
  - name: "Euphoric Breath"
    desc: "`pf2:2` The dragonet breathes euphoric gas in a @Template[cone|distance:15]. Each creature in the area must succeed at a DC 18 [[Fortitude]] save or become [[Stupefied 2]] and [[Slowed]] 1 for 1d4 rounds; on a critical failure, the duration is 1 minute. <br>  <br> The fey dragonet can't use Euphoric Breath again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Although they are much smaller than their larger dragon cousins, fey dragonets have many of the same physiological attributes, including long necks, toothy maws, sinuous tails, and sharp claws. They flit about on iridescent butterfly wings, the coloring of which changes based on where they live, giving them a natural camouflage. Unlike their larger kin, an adult fey dragonet remains the same size throughout their lifespan. The only visual clue to the age of a fey dragonet is the sheen on their scales, a glimmer that becomes more lustrous the older they get.

Fey dragonets usually exhibit pleasant and good-natured temperaments, though they have a mischievous streak that leads them to play tricks on those around them. In search of amusement, they prefer harmless annoyances over wounding malice. While often spontaneous, they may also spend months, if not years, planning the perfect prank. Especially responsive targets endear themselves to fey dragonets and may create a lifelong bond. A fey dragonet's reputation as a trickster leads many to associate them with fey, with whom the tiny dragons have cordial relationships, and this association gives them their name.

Peaceful by nature, fey dragonets don't enjoy confrontation. If faced with hostility, they prefer to remain at a distance and breathe euphoric gas at their foes, diffusing the skirmish by creating an atmosphere of bliss. If conflict escalates, they target their opponents with spells, using their renowned trickery to escape. If their companions are in danger, however, their desire to remain out of combat changes. Fey dragonets protect their friends by any means available, including physical combat.

Sometimes, as fey dragonets grow older, their connection to the First World grows stronger. In addition to growing more lustrous and vibrant in appearance, these fey dragonets gain an increasing amount of magical primal power. Such fey dragonets increase in strength as appropriate—a fey dragonet of 20th level or even higher is possible, but it's exceptionally unusual to encounter a fey dragonet of 9th level or higher beyond the most remote regions of the First World. When creating a more powerful fey dragonet, change their spellcasting tradition to primal and grant them primal spells appropriate for a druid of their level. Fey dragonets don't grow much larger, regardless of how powerful they become. It's often difficult to tell how powerful one of these tiny dragons truly is at a glance!

```statblock
creature: "Fey Dragonet"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
