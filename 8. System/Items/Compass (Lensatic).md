---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 20}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A compass helps you [[Sense Direction]] or navigate, provided you're in a location with uniform magnetic fields. Without a compass, you take a -2 item penalty to these checks (similar to using a shoddy item).

A lensatic compass gives you a +1 item bonus to these checks.

**Source:** `= this.source` (`= this.source-type`)
