---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Backstabber]]", "[[Fatal d10]]", "[[Goblin]]", "[[Scatter 5]]"]
price: "{'gp': 5}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A flingflenser is a goblin-designed weapon ending in an ovoid tube with a hatch and handle on the narrow end. A cluster of circular blades held together and attached to a black powder packet with a thin leather strap serves as ammunition and is loaded through the hatch before being fired with a flintlock or other external ignition mechanism. The flingflenser's sturdy design also places it among the more reliable goblin weapons.

**Source:** `= this.source` (`= this.source-type`)
