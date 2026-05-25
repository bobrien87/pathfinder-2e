---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Consumable]]", "[[Divine]]"]
price: "{'gp': 600}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This thin golden candle bears the symbol of a specific deity emblazoned on its surface, surrounded by the iconography of that deity's faith. A *taper of sanctification* must be dedicated to a deity who can be sanctified to holy or unholy, and has the corresponding trait. If the deity's sanctification lists both options, the crafter must choose one when the candle is made.

Once lit, this candle burns for 1 hour, and it can't be extinguished. When a willing creature spends the full hour within 10 feet of the lit candle engaging in prayer to the deity, that creature's Strikes gain the holy or unholy trait (as appropriate for the candle) until the next time that creature makes their daily preparations. During this time, the creature is bound by the deity's anathema. If they violate anathema, they lose the benefit of the *taper of sanctification*. A holy creature can't benefit from an unholy *taper of sanctification*, nor can an unholy creature benefit from a holy one.

> [!danger] Effect: Taper of Sanctification

**Source:** `= this.source` (`= this.source-type`)
