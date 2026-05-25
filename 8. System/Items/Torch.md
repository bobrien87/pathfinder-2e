---
type: item
source-type: "Remaster"
level: "0"
price: "{'cp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A torch sheds bright light in a 20-foot radius (and dim light to the next 20 feet) for 1 hour. It can be used as an improvised weapon that deals 1d4 bludgeoning damage plus 1 fire damage.

**Source:** `= this.source` (`= this.source-type`)
