---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Catfolk|Catfolk]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You come from a long line of skilled hunters and trackers and have a particularly keen sense of smell. You gain imprecise scent with a range of 30 feet. This means you can use your sense of smell to determine a creature's location. The GM will usually double the range if you're downwind from the creature or halve the range if you're upwind.

In addition, you gain a +2 circumstance bonus to [[Track]] a creature or object if you've smelled it before.

**Source:** `= this.source` (`= this.source-type`)
