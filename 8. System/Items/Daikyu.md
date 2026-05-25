---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Forceful]]", "[[Propulsive]]"]
price: "{'gp': 8}"
usage: "held-in-one-plus-hands"
bulk: "2"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This asymmetrical bow, made of laminated bamboo, wood, and leather, stands 6 feet or more in height. It's most often used while mounted.

**Source:** `= this.source` (`= this.source-type`)
