---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Cold]]", "[[Magical]]"]
price: "{'gp': 500}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This weapon is empowered with freezing ice. It deals an additional 1d6 cold damage on a successful Strike. On a critical hit, the target is also [[Slowed]] 1 until the end of your next turn unless it succeeds at a DC 24 [[Fortitude]] save.

**Source:** `= this.source` (`= this.source-type`)
