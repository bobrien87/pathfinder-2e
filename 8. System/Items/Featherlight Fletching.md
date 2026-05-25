---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 20, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Elven archers were the first to create the *featherlight fletching*, meant for long-range battles, though artisans of many other ancestries have now learned the art of crafting these whetstones. A *featherlight fletching* is a feather-shaped trinket crafted of spun silver filigree and aids projectiles in flying true, even over great distances. A ranged weapon under the effects of a *featherlight fletching* doubles its range increment for 1 minute.

> [!danger] Effect: Featherlight Fletching

**Source:** `= this.source` (`= this.source-type`)
