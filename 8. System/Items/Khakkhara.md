---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Shove]]", "[[Two hand d10]]", "[[Versatile p]]"]
price: "{'gp': 2}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This staff is topped by a pointed metal circle from which hang several smaller rings that jingle and clang noisily as the staff is moved, allowing you to announce your presence and scare off wild animals as you walk.

**Source:** `= this.source` (`= this.source-type`)
