---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Dwarf]]", "[[Sweep]]", "[[Two hand d12]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "2"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This favored weapon of the dwarves has a large, ornate head mounted on a thick handle. This powerful axe can be wielded with one hand or two.

**Source:** `= this.source` (`= this.source-type`)
