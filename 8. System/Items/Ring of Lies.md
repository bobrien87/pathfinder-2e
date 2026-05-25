---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 850}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This plain silver ring has an almost oily sheen. While wearing the ring, you gain a +2 item bonus to Deception checks.

**Activate—Sweeten Lies** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** Snapping your fingers on the hand that wears the ring causes the ring to cast [[Honeyed Words]] on you with no visual manifestations of a spell being cast.

**Source:** `= this.source` (`= this.source-type`)
