---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Clockwork]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "16"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Clockwork timepieces come in a variety of sizes and aesthetic styles, but they're all designed to display the accurate time of day down to the second.

Clockwork timepieces have a 24-hour activation cycle, after which they must wound in a process that takes 1 minute to complete.

These towering, ten-foot-tall clocks have been painstakingly handcrafted by skilled artisans and feature loud chimes that can be heard hourly throughout a manor. Owners of grand clocks usually tend to display them prominently in a study, lounge area, or foyer.

**Source:** `= this.source` (`= this.source-type`)
