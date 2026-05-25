---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Bulwark]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 2000}"
bulk: "4"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 resilient full plate* is crafted from the most colorful fragments chipped from scales of a dragon turtle's shell, traditionally incorporating that motif in the form of a thicker, sturdier backplate. While wearing this armor, you aren't [[Off Guard]] from creatures that flank you, and you ignore the armor's Speed penalty when you Swim and its check penalty to Athletics checks to Swim.

**Source:** `= this.source` (`= this.source-type`)
