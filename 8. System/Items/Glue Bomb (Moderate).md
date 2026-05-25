---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

A glue bomb is a harmless explosive mechanism bursting with sticky substances. When you hit a creature with a glue bomb, that creature takes a –15-foot status penalty to its Speeds for 1 minute. You gain a +1 item bonus to attack rolls, and the [[Escape]] DC is 19.

On a critical hit, a creature in contact with a solid surface becomes stuck to the surface and [[Immobilized]] for 1 round, and a creature flying via wings has its wings tangled, causing it to fall safely to the ground and become unable to Fly again for 1 round. Glue bombs are not effective when used on a creature that is in water.

The target can end any effects by Escaping or spending a total of 3 Interact actions to carefully remove the sticky substances. These Interact actions don't have to be consecutive, and other creatures can provide the actions as well.

> [!danger] Effect: Glue Bomb

**Source:** `= this.source` (`= this.source-type`)
