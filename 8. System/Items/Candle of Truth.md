---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Magical]]", "[[Mental]]"]
price: "{'gp': 75}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

This tapered candle has a golden wick that burns with white fire. You activate the candle by lighting it, which causes creatures within 10 feet of the candle to find it difficult to tell falsehoods. Creatures in the area receive a –4 status penalty to Lie.

In addition, when first entering the affected area, each creature (including you) must succeed at a DC 26 [[Will]] save or be unable to tell any deliberate lies while within 10 feet of the lit candle. This lasts for as long as the candle is lit. Once lit, the candle burns for 10 minutes, and it cannot be extinguished.

**Source:** `= this.source` (`= this.source-type`)
