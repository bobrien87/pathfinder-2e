---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]", "[[Visual]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Using bioluminescent matter or alchemical reagents, you rig a short-lived flare to a trip wire or pressure plate. When a Small or larger creature enters the square, this flare shoots into the sky. To creatures with a clear view of the sky, this flare is visible from up to 2 miles away on a clear day or up to 5 miles away on a clear night.

**Source:** `= this.source` (`= this.source-type`)
