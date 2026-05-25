---
type: item
source-type: "Remaster"
level: "2"
price: "{'gp': 25}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This is a 2-foot-long tube with two angled mirrors, one at each end. When the mirrors are aligned correctly, you can look around obstacles while remaining behind cover. This doesn't provide a sufficient line of effect to target creatures around corners.

**Source:** `= this.source` (`= this.source-type`)
