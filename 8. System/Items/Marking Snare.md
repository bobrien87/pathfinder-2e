---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This snare is often used to mark intruders for later tracking or identification. When you create this snare, you must decide whether to make it a dye or a scent marker. Either type of marking grants a +2 circumstance bonus to [[Track]] the creature for up to 24 hours or until the dye or scent is washed off (requiring at least a gallon of water and 10 minutes of scrubbing). A creature that enters a square of the snare must attempt a [[Reflex]] save.
- **Success** The creature is unaffected.
- **Failure** The snare marks the creature.
- **Critical Failure** The snare marks the creature, and the creature is [[Blinded]] until the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)
