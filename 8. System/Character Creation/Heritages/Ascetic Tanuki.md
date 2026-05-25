---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Tanuki|Tanuki]]"
traits: ["[[Tanuki]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

It's said your round form is the result of calmness and restraint, not indulgence. You gain scent as an imprecise sense with a range of 30 feet. The GM will usually double the range if you're downwind from something you're trying to smell or halve the range if you're upwind. In addition, you gain a +2 circumstance bonus to Perception checks whenever you're trying to locate food, drink, or a consumable item that's ingested (such as a potion or elixir) using your scent.

**Source:** `= this.source` (`= this.source-type`)
