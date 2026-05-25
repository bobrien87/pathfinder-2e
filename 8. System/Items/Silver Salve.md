---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 6}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

You can slather this silvery paste onto one melee weapon, one thrown weapon, or 10 pieces of ammunition. Silver salve spoils quickly, so once you open a vial, you must use it all at once, rather than saving it.

For the next hour, the weapon or ammunition counts as silver instead of its normal material (such as cold iron) for any physical damage it deals.

> [!danger] Effect: Silver Salve

**Source:** `= this.source` (`= this.source-type`)
