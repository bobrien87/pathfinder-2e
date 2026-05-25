---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 4}"
usage: "other"
bulk: "2"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Tack includes all the gear required to outfit a riding animal, including a saddle, bit and bridle, and stirrups if necessary. Especially large or oddly shaped animals might require specialty saddles. These can be more expensive or hard to find, as determined by the GM. The Bulk value given is for tack worn by a creature. If carried, the Bulk increases to 2.

**Source:** `= this.source` (`= this.source-type`)
