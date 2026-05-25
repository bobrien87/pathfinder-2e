---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Shove]]"]
price: "{'gp': 1}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This weapon has a wooden shaft ending in a large, heavy metal head. The head of the hammer might be single-sided or double-sided, but it's always capable of delivering powerful bludgeoning blows.

**Source:** `= this.source` (`= this.source-type`)
