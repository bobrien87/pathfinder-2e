---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Sweep]]"]
price: "{'sp': 4}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This simple axe is created by inserting a weighted metal wedge into a curved wooden handle with a Y-shaped groove at the top, and then binding the splitting wedge in place with leather thongs.

**Source:** `= this.source` (`= this.source-type`)
