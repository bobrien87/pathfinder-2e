---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Darkness]]", "[[Magical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 15}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When a creature enters the snare's square, it is plunged into an unnatural darkness for 1 minute. Light can't enter the square, any non-magical light sources within the square do not emanate any light, and magical light emanating from a spell of rank 2 or below is suppressed. Those outside the area can't see directly into or through the darkness, and all adjacent squares are reduced to dim light.

**Source:** `= this.source` (`= this.source-type`)
