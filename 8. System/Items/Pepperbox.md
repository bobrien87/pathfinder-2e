---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Capacity 3]]", "[[Concussive]]", "[[Fatal d8]]"]
price: "{'gp': 9}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This weapon is a specialty of the smiths of Alkenstar. The pepperbox has three barrels that each hold a single shot, and the shooter can manually rotate the whole barrel assembly to align a loaded barrel with the firing mechanism.

**Source:** `= this.source` (`= this.source-type`)
