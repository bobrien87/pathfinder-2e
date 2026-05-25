---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Fire]]", "[[Magical]]"]
price: "{'gp': 90}"
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

This stubby, black candle has a wick made of a type of flammable bronze that can be found only on the Plane of Fire. You activate the candle by lighting it, which enables creatures within @Template[emanation|distance:10]{10 feet} of the candle to ignore the cold while within range. Creatures in the area gain cold resistance 10. In addition, a creature taking persistent cold damage that is in or enters the area can immediately attempt a DC 15 flat check to end the persistent damage. A given creature can gain this flat check only once from a single *thawing candle*. Once lit, the candle burns for 10 minutes. If extinguished, it can't be relit.

> [!danger] Effect: Thawing Candle

**Source:** `= this.source` (`= this.source-type`)
