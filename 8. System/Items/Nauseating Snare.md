---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Poison]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 40}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You position particularly foul substances to splash over a creature. The first creature to enter the square must attempt a [[Fortitude]] save saving throw.
- **Critical Success** The creature is unaffected.
- **Success** The creature becomes [[Sickened]] 1.
- **Failure** The creature becomes [[Sickened]] 2.
- **Critical Failure** The creature becomes [[Sickened]] 3.

**Source:** `= this.source` (`= this.source-type`)
