---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 55}"
usage: "worn"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Fine clothing, suitable for a noble or royal, is made with expensive fabrics, precious metals, and intricate patterns. You gain a +1 item bonus to checks to Make an Impression on nobility or other upper-class folk while wearing high-fashion fine clothing.

**Source:** `= this.source` (`= this.source-type`)
