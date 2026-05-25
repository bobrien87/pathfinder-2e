---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hunter"
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
    desc: "+17"
languages: "Common"
skills:
  - name: Skills
    desc: "Medicine +15, Nature +17, Stealth +17, Survival +17, Forest Lore +13"
abilityMods: ["+4", "+4", "+2", "+1", "+4", "+0"]
abilities_top:
  - name: "Expert Subsistence"
    desc: "While using Survival to `act subsist statistic=survival`, if the hunter rolls any result worse than a success, they get a success. On a success, they can provide subsistence living for themselves and 16 additional creatures, and on a critical success, they can take care of twice as many creatures as on a success."
  - name: "Forest Walker"
    desc: "The hunter ignores the effects of difficult terrain in a forest environment."
armorclass:
  - name: AC
    desc: "25; **Fort** +12, **Ref** +17, **Will** +15"
health:
  - name: HP
    desc: "115"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +17 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+10 piercing"
  - name: "Melee strike"
    desc: "Fist +17 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
  - name: "Melee strike"
    desc: "Dagger +17 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+10 piercing"
  - name: "Ranged strike"
    desc: "Composite Longbow +18 (`pf2:1`) (deadly d10, magical, propulsive, reload 0, volley 30, range 100 ft.), **Damage** 1d8+8 piercing"
spellcasting: []
abilities_bot:
  - name: "On the Hunt"
    desc: "`pf2:1` The hunter designates one creature they're observing or tracking as their prey. <br>  <br> The hunter gains a +2 circumstance bonus to Perception checks to `act seek` the prey and to Survival checks to `act track` the prey. <br>  <br> The first time the hunter hits the designated prey in a round, they deal an additional 1d8 precision damage. These effects last until the hunter uses On the Hunt again."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

As is reflected in the many depictions of the elk-headed Erastil, god of the hunt, the hunter is very much a creature of the forest, known by the forest and familiar with every aspect of it. After all, the final determination of who is the hunter and who is prey often depends on who can make an ally of the terrain.

Explorers are often well-equipped and well-trained for any type of hazard and are eager to lead others into the wild.

```statblock
creature: "Hunter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
