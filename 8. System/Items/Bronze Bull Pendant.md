---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 7}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (concentrate)

This pendant is forged from grainy steel and depicts a snorting bull's face. The pendant must be attached to the chest area or on a shoulder guard. When you activate the pendant, attempt an Athletics check to [[Shove]] with a +1 item bonus to check. Increase the distance you Shove your target to 10 feet on a success or 20 feet on a critical success.

> [!danger] Effect: Bronze Bull Pendant

**Source:** `= this.source` (`= this.source-type`)
