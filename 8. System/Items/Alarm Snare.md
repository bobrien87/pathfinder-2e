---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Auditory]]", "[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
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

You create an alarm snare by rigging one or more noisy objects to a trip wire or pressure plate. When you create an alarm snare, you designate a range between 100 to 500 feet at which it can be heard. When a Small or larger creature enters the square, the snare makes a noise loud enough that it can be heard by all creatures in the range you designated.

**Source:** `= this.source` (`= this.source-type`)
