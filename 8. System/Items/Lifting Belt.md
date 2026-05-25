---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 80}"
usage: "wornbelt"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wide leather belt grants you a +1 item bonus to Athletics checks and increases the amount you can easily carry. You can carry Bulk equal to 6 + your Strength modifier before becoming encumbered, and you can hold and carry a total Bulk up to 11 + your Strength modifier.

**Activate—Assisted Lift** `pf2:2` (manipulate)

**Effect** You lift an object of up to 8 Bulk as though it were weightless. This requires two hands, and if the object is locked or otherwise held in place, you can attempt to Force it Open using Athletics as part of this activation. The object still has its full weight and Bulk for all other purposes-you just ignore that weight. The effect lasts until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
