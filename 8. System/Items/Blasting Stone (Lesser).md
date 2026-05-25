---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Sonic]]", "[[Splash]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

When this pebble hits a creature or a hard surface, it explodes with a deafening bang. A blasting stone deals 1d4 sonic damage and 1 sonic splash damage, and each creature within 10 feet of the space in which the stone exploded must succeed at a DC 17 [[Fortitude]] save saving throw with the listed DC or be [[Deafened]] until the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)
