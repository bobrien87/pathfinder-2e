---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

A shimmering liquid, *nectar of purification* is often stored in bottles similar to those used for vinegar. This oil casts a 1st-rank [[Cleanse Cuisine]] spell over any food or drink onto which it's poured. The nectar evaporates as it takes effect, leaving the taste and texture of the food or drink unaltered.

**Source:** `= this.source` (`= this.source-type`)
