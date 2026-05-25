---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 55}"
usage: "held-in-two-hands"
bulk: "6"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You need an alchemist's lab to Craft alchemical items during downtime.

An expanded alchemist's lab gives a +1 item bonus to Crafting checks to create alchemical items.

**Source:** `= this.source` (`= this.source-type`)
