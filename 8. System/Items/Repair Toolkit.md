---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 2}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A repair kit allows you to perform simple repairs while traveling. It contains a portable anvil, tongs, woodworking tools, a whetstone, and oils for conditioning leather and wood. You can use a repair kit to Repair items using the Crafting skill. You can draw and replace a worn repair toolkit as part of the action that uses it.

**Source:** `= this.source` (`= this.source-type`)
