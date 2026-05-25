---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These four-pronged metal spikes can damage a creature's feet. You can scatter caltrops in an empty square adjacent to you with an Interact action. The first creature that moves into that square must succeed at a DC 14 [[Acrobatics]] check or take 1d4 piercing damage and 1 persistent bleed damage. A creature taking persistent bleed damage from caltrops takes a –5-foot penalty to its Speed. Spending an Interact action to pluck the caltrops free reduces the DC to stop the bleeding. Once a creature takes damage from caltrops, enough are ruined that other creatures moving into the square are safe. Deployed caltrops can be salvaged and reused if no creatures took damage from them. Otherwise, enough are ruined that they can't be salvaged.

> [!danger] Effect: Caltrops

**Source:** `= this.source` (`= this.source-type`)
