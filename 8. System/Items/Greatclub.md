---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Backswing]]", "[[Shove]]"]
price: "{'gp': 1}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While many greatclubs are intricately carved, others are little more than a sturdy tree branch. These massive clubs are too heavy to wield with only one hand.

**Source:** `= this.source` (`= this.source-type`)
