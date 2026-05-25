---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Combination]]", "[[Concealable]]", "[[Concussive]]", "[[Fatal d8]]"]
price: "{'gp': 8}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This fashionable cane's handle hides a dueling pistol fired through the thin, painted cap at the bottom of the cane.

**Source:** `= this.source` (`= this.source-type`)
