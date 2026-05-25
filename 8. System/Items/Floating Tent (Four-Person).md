---
type: item
source-type: "Remaster"
level: "2"
price: "{'gp': 25}"
usage: "other"
bulk: "1"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This diamond-shaped tent is designed for sleeping in planar environments without gravity, such as the Plane of Air. Weights are attached at each of its six points, carefully balanced against each other to prevent the tent from leaning too far in any one direction. The tent has an anchor, which can be used to moor the tent and prevent it from floating away from the object or location it is anchored to.

A standard floating tent is large enough for four creatures and their supplies, containing four hammocks in two rows suspended in the center of the tent and large nets near the top and bottom of the tent for gear.

**Source:** `= this.source` (`= this.source-type`)
