---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 10}"
bulk: "4"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These massive shields can be used to provide cover to nearly the entire body. Due to their size, they are typically made of wood reinforced with metal. AC increases to +4 if you are using the [[Take Cover]] action.

Hardness
HP
BT

5
20
10

**Source:** `= this.source` (`= this.source-type`)
