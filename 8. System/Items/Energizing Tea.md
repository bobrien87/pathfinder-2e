---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]", "[[Tea]]"]
price: "{'gp': 20}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This sweet and refreshing tea is made with a mixture of honey, lemon slices, and sliced ginger. This is considered to be the bare minimum when serving *energizing tea*, and many go above and beyond by adding additional citrus fruits or berries to the mix or refusing to serve the tea at all without also serving a full platter of spiced pastries and sweets. This golden tea has energizing properties and, when consumed, grants you a +1 item bonus to Athletics and Acrobatics checks for 10 minutes.

> [!danger] Effect: Energizing Tea

**Activate—Tea Ceremony** 10 minutes (concentrate, manipulate) The duration increases to 1 hour.

**Source:** `= this.source` (`= this.source-type`)
