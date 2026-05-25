---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 7}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A lantern sheds bright light and requires 1 pint of oil to function for 6 hours. A hooded lantern sheds light in a 30-foot radius (and dim light in the next 30 feet) and is equipped with shutters, which you can close to block the light. Closing or opening the shutters takes an Interact action.

**Source:** `= this.source` (`= this.source-type`)
