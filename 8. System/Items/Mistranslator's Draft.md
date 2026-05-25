---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Cursed]]", "[[Magical]]", "[[Potion]]"]
price: "{'per': 1, 'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A pickled lizard's tongue, tied into a knot, floats in this oily potion. When you drink it, you can speak and understand all spoken (but not written) languages for 1 hour. However, if you attempt to translate any spoken language, your translation is always erroneous in a way likely to cause substantial confusion or anger, typically reducing the listener's attitude toward you by one step. You aren't aware of your error, and any attempt to correct the mistake only compounds it.

**Source:** `= this.source` (`= this.source-type`)
