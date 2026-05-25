---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 15}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You set a cunning wire to trip a creature. A Medium or smaller creature that enters this snare's square must attempt a [[Reflex]] save.

If you want to create a trip snare to trip a larger creature, you must create a group of contiguous snares of a length equal to the edge of that larger creature's space, and the creature must be moving such that it moves into the full set of snares. For example, three trip snares in a 15-foot-line can trip a Huge creature coming down a corridor into the line of snares.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Off Guard]] until the start of its next turn.
- **Failure** The creature falls [[Prone]].
- **Critical Failure** The creature falls prone and takes 1d6 bludgeoning damage.

**Source:** `= this.source` (`= this.source-type`)
