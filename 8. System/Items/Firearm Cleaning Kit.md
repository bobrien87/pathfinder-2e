---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 1}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This kit contains cleaning cloth, oil, small steel brushes, and other minor tools necessary for proper cleaning and maintenance of a firearm. Without a firearm cleaning kit, you can't perform the necessary tasks during your daily preparations to ensure that your firearm isn't at risk of misfiring under normal use conditions.

**Source:** `= this.source` (`= this.source-type`)
