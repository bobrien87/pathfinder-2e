---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Disarm]]", "[[Finesse]]", "[[Trip]]"]
price: "{'gp': 3}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This 4-foot-long length of chain is covered with barbs and has spikes on one or both ends. Some feature metal hoops used as handgrips.

**Source:** `= this.source` (`= this.source-type`)
