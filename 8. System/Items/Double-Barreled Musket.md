---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Concussive]]", "[[Double barrel]]", "[[Fatal d10]]"]
price: "{'gp': 11}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This flintlock breech-loader has two side-by-side barrels. Though less accurate than a standard musket, a double-barreled musket offers versatility in firing options. Many of Alkenstar's famous shield marshals save their earnings to buy a double-barreled musket as their first personal firearm.

**Source:** `= this.source` (`= this.source-type`)
