---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Combination]]", "[[Monk]]", "[[Propulsive]]"]
price: "{'gp': 8}"
usage: "held-in-one-plus-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The mikazuki combines a sansetsukon with a thin length of metal string and several locking mechanisms built into the joints, allowing it to be quickly locked into configuration as a bow.

**Source:** `= this.source` (`= this.source-type`)
