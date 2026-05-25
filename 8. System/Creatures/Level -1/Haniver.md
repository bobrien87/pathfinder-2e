---
type: creature
group: ["Amphibious", "Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Haniver"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Amphibious"
trait_02: "Fey"
trait_03: "Gremlin"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: "Common, Sakvroth, Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +5, Deception +4, Nature +3, Stealth +5, Thievery +5"
abilityMods: ["+1", "+3", "+2", "-1", "+1", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +4, **Ref** +7, **Will** +3"
health:
  - name: HP
    desc: "8; **Weaknesses** cold iron 2"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bite +7 (`pf2:1`) (agile, finesse), **Damage** 1d4 + 1 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 13, attack +5<br>**1st** [[Fear]], [[Prestidigitation]], [[Ventriloquism]]"
abilities_bot:
  - name: "Rearrange Possessions"
    desc: "`pf2:1` `pf2:1` or `pf2:2` <br>  <br> The haniver attempts to [[Steal]] a small object off a target's person. <br>  <br> If they succeed, they also rifle through and rearrange the contents of the target's pockets, pouches, and other containers. The next time the target attempts to draw a weapon or retrieve a worn item, doing so requires 2 Interact actions instead of one. <br>  <br> The haniver can Steal an object that's closely guarded using this action without the –5 penalty, though not objects that would be extremely noticeable or time-consuming to remove. They can spend 2 actions instead of 1 to use this ability to Steal from a creature in combat or otherwise on guard."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Hanivers are the most benign type of gremlin—capricious fey who skim the waves on rubbery fin-wings. Though they don't actively sabotage their environment, sailors bemoan these gremlins' grasping fingers. Hanivers' incessant curiosity compels them to examine any object that draws their attention. Such treasures might include overturned fruit baskets, sacks of coins, or the gleaming teeth of a shark (often still in the shark's mouth, to the fey's regret). Should hanivers like what they find, they steal it, making them a bane to fishers and dockworkers everywhere.

Gremlins arose long ago in the First World, living embodiments of nature's ability to wear away, erode, and decompose. In the Universe, their encounters with mortal civilizations twisted them into creatures devoted to chaos, sabotage, and traps, each variety specializing in a particular brand of mayhem.

```statblock
creature: "Haniver"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
