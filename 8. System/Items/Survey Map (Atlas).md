---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 50}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Maps are uncommon. Most maps you can find are simple and functional. A survey map details a single location in excellent detail.

One of these maps gives you a +1 item bonus to Survival checks and any skill checks to Recall Knowledge, provided the checks are related to the location detailed on the map.

Maps sometimes come in atlases, containing a number of maps of the same quality, often on similar topics. An atlas costs five times as much as a single map and requires both hands to use.

The GM determines what maps are available in any location.

**Source:** `= this.source` (`= this.source-type`)
