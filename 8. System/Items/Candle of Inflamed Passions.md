---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Fire]]", "[[Magical]]", "[[Mental]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This blood-red candle is made from wax derived from oil shale found in certain parts of the Plane of Fire. The wick burns with a flame that flickers and dances even if there's no draft to stir it. You activate the candle by lighting it, which causes creatures within 10 feet of the candle to find their emotions running high. Creatures in the area take a -1 status penalty to saving throws against emotion effects. Once lit, the candle burns for 10 minutes. If extinguished, it can't be relit.

**Source:** `= this.source` (`= this.source-type`)
