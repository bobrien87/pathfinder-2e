---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Catfolk]]", "[[Deadly d8]]", "[[Disarm]]", "[[Finesse]]", "[[Versatile p]]"]
price: "{'gp': 2}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This handheld weapon's three parallel blades extend between the fingers to resemble the natural claws of the amurruns who created them, providing a way for those catfolk without suitable natural claws to share the fighting customs of their kin.

**Source:** `= this.source` (`= this.source-type`)
