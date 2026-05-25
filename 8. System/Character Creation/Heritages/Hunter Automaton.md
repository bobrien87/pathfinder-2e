---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Automaton|Automaton]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You were designed to serve as a scout or assassin and have a body resembling a pack hunter like a large cat or wolf. Though you typically move like a quadruped, you can still stand and fight like a biped, allowing you to use all equipment normally. Your quadruped design allows you to move quickly; if you have both hands free, you can increase your Speed to 30 feet as you run on all fours.

**Source:** `= this.source` (`= this.source-type`)
