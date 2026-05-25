---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Kholo|Kholo]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You're a nimble-bodied kholo with a prehistoric, almost dog-like build. Though you typically move like a quadruped, you can still stand and fight like a biped, allowing you to use all equipment normally. If you have both hands free, you can increase your Speed to 30 feet as you run on all fours.

**Source:** `= this.source` (`= this.source-type`)
