---
type: item
source-type: "Remaster"
level: "0"
price: "{'value': {}}"
usage: "other"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These displays are designed to create distinctive effects you can use to make onlookers marvel and even to gain an advantage in combat.

*Note: This item is to be used by the Firework Technician archetype.*

**Source:** `= this.source` (`= this.source-type`)
