---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fleshwarper"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13"
languages: "Common, Sakvroth"
skills:
  - name: Skills
    desc: "Crafting +17, Medicine +16, Occultism +15, Stealth +15, Aberration Lore +15, Fleshwarping Lore +17"
abilityMods: ["+3", "+4", "+2", "+4", "+2", "-1"]
abilities_top:
  - name: "Flesh Mutation"
    desc: "A creature made of flesh that's hit by a fleshwarping concoction Strike is subject to a random fleshwarping mutation determined by rolling 1d4 and consulting the list below. The creature attempts a DC 25 [[Fortitude]] save at the end of each of its turns, ending the mutation on a success. A creature that becomes mutated is thereafter temporarily immune to flesh mutation for 1 day. <br>  <br> **1 Spongy Flesh** The creature has weakness 5 to physical damage. <br>  <br> **2 Caustic Blood** The creature takes 2d4 persistent acid damage that can't be removed normally, but ends when the mutation does. <br>  <br> **3 Sprouting Eyes** The creature is [[Dazzled]], but also immune to flanking. <br>  <br> **4 Mutated Mind** The creature is [[Confused]]. It can still recover as noted in the condition, but if it does it remains [[Off Guard]] until the mutation ends. <br>  <br> > [!danger] Effect: Flesh Mutation"
armorclass:
  - name: AC
    desc: "24; **Fort** +15, **Ref** +15, **Will** +15"
health:
  - name: HP
    desc: "110"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scalpel +18 (`pf2:1`) (agile, finesse, magical, versatile s), **Damage** 1d4+9 piercing"
  - name: "Melee strike"
    desc: "Scalpel +18 (`pf2:1`) (agile, magical, thrown 10, versatile s), **Damage** 1d4+9 piercing"
  - name: "Melee strike"
    desc: "Fist +17 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+9 bludgeoning"
  - name: "Ranged strike"
    desc: "Fleshwarping Concoction +17 (`pf2:1`) (alchemical, poison, range 20 ft.), **Damage** 4d6 poison plus [[Flesh Mutation]]"
spellcasting: []
abilities_bot:
  - name: "Conduct the Experiment"
    desc: "`pf2:1` The fleshwarper assesses vulnerabilities in a creature's anatomy. They attempt a [[Medicine]] check against the Fortitude DC of one living creature they can see within 60 feet. On a success, the fleshwarper's melee Strikes deal an extra 2d8 precision damage against that creature for 1 minute or until the fleshwarper critically hits that creature, whichever comes first. <br>  <br> Using this action again designates a new target and ends the effect for any previous target. A fleshwarper can target an individual no more than once per day with this ability. <br>  <br> > [!danger] Effect: Conduct the Experiment"
  - name: "Restore My Masterpiece"
    desc: "`pf2:1` **Requirements** The fleshwarper is holding or wearing a healer's toolkit <br>  <br> **Effect** The fleshwarper stitches the wounds of an adjacent, willing aberration or creature they modified using fleshwarping. The creature regains 20 healing HP and is then temporarily immune for 1 day."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Cruel scientists called fleshwarpers create horrors from the flesh of others. Many desire to push science forward, but others need only grotesque glee.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Fleshwarper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
