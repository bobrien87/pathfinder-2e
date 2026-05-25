---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 1500}"
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

Upon drinking this clear, refreshing potion, you can see things as they actually are. You gain the benefits of a 7th-rank [[Truesight]] spell that has a counteract modifier of `r 1d20+25`.

**Source:** `= this.source` (`= this.source-type`)
