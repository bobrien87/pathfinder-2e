---
type: creature
group: ["Aberration", "Goblin"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gobmob Snake"
level: "4"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: "Goblin"
trait_03: "Mutant"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Common, Goblin (snake empathy)"
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +10, Intimidation +9, Stealth +12, Survival +8"
abilityMods: ["+3", "+5", "+2", "-2", "+1", "+2"]
abilities_top:
  - name: "Snake Empathy"
    desc: "A gobmob snake can communicate with snakes."
armorclass:
  - name: AC
    desc: "21; **Fort** +12, **Ref** +13, **Will** +8"
health:
  - name: HP
    desc: "60"
abilities_mid:
  - name: "Coiled Strike"
    desc: "`pf2:r` As [[Reactive Strike]], but the gobmob snake can use this reaction only if it's Coiled."
  - name: "Incessant Yammering"
    desc: "15 feet. <br>  <br> A gobmob snake's heads constantly bicker and snipe at one another, annoying and distracting anyone nearby. Each non-goblin creature that begins its turn in the aura must attempt a DC 21 [[Will]] save. On a failure, it takes a –1 status penalty to Perception checks and Will saves for 1 round. On a success, it is temporarily immune for 1 minute. <br>  <br> > [!danger] Effect: Incessant Yammering"
  - name: "Infighting"
    desc: "Whenever a gobmob snake critically fails at an attack roll or skill check, it must succeed at a DC 5 flat check or become [[Slowed]] 1 as its heads argue over which of them is to blame. An enemy can provoke an argument by attempting a DC 20 [[Deception]] check as a single action with the auditory, concentrate, linguistic, and mental traits."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +14 (`pf2:1`) (finesse, unarmed), **Damage** 2d6+5 piercing"
spellcasting: []
abilities_bot:
  - name: "Coil"
    desc: "`pf2:1` The gobmob snake uses an action to coil itself, increasing its reach with its fangs from 5 to 10 feet. After the gobmob snake Strikes with its fangs, it becomes uncoiled."
  - name: "Goblin Breath"
    desc: "`pf2:2` The gobmob snake belches a cloud of nauseating vapor in a @Template[type:cone|distance:15]. Non-goblin creatures within the cloud must succeed at a DC 20 [[Fortitude]] save or become [[Sickened]] 1. On a critical failure, a creature is also [[Slowed]] 1 for as long as it is sickened. Creatures that successfully save are immune for 24 hours. The gobmob snake can't use Goblin Breath again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These bizarre mutant goblin snakes possess no fewer than three heads.

A goblin snake is a foul-smelling serpentine creature covered in greasy black scales and sporting a fanged, lipless head resembling that of a goblin.

```statblock
creature: "Gobmob Snake"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
