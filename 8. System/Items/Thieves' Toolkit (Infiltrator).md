---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 50}"
usage: "other"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You need a thieves' toolkit to [[Pick Locks]] or [[Disable Devices]] (of some types) using the Thievery skill. An infiltrator thieves' toolkit add a +1 item bonus to checks to Pick Locks and Disable Devices.

If your thieves' toolkit is broken, you can repair it by replacing the lock picks with Replacement Picks appropriate to your tools; this doesn't require using the Repair action. If you wear your thieves' toolkit, you can draw and replace it as part of the action that uses it.

**Source:** `= this.source` (`= this.source-type`)
