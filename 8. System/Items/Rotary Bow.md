---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Capacity 4]]"]
price: "{'gp': 8}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This one-handed crossbow has four arms instead of two, and four rotating chambers that can be pre-loaded with bolts for more efficient firing. The chamber can be swapped and the arms redrawn with a simple crank device built into the crossbow.

**Source:** `= this.source` (`= this.source-type`)
