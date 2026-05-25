---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Forceful]]", "[[Sweep]]", "[[Tripkee]]"]
price: "{'gp': 1}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A common cutting tool, an adze resembles an axe—but the cutting edge is horizontal, rather than vertical. The adze's shape makes it popular among woodworkers, and tripkee builders often use them to construct their treetop homes. The tool also serves as an effective weapon, due in part to the immense strength required to swing it.

**Source:** `= this.source` (`= this.source-type`)
