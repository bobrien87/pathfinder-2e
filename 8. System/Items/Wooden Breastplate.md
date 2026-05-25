---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 6}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A suit of carved and tempered wood, a wooden breastplate resembles a metal breastplate in shape and function. Such suits can be carved from large pieces of wood, but they most often come from wood coaxed magically from special trees, whether by druids, elves, fey, or plant creatures such as arboreals or leshies.

**Source:** `= this.source` (`= this.source-type`)
