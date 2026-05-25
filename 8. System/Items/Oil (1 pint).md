---
type: item
source-type: "Remaster"
level: "0"
price: "{'cp': 1}"
usage: "held-in-two-hands"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You can use oil to fuel lanterns, but you can also set a pint of oil aflame and throw it. You must first spend an Interact action preparing the oil, then throw it with another action as a ranged attack. If you hit, it splatters on the creature or in a single 5-foot square you target. You must succeed at a DC 10 flat check for the oil to ignite successfully when it hits. If the oil ignites, the target takes 1d6 fire damage.

**Source:** `= this.source` (`= this.source-type`)
