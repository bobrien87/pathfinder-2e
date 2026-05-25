---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Orc|Orc]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You were exposed to powerful necromantic energies that should have killed you—but you survived. Your skin is cold, clammy, and gray. You gain resistance to void damage equal to half your level (minimum 1). You also gain a +1 circumstance bonus to saving throws against effects with the death or void trait.

**Source:** `= this.source` (`= this.source-type`)
