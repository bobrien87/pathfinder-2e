---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Bomb]]", "[[Consumable]]", "[[Force]]", "[[Splash]]"]
price: "{'gp': 19}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

Aether marbles create violent, lingering eddies of force that extend partially into unseen planes. You gain a +1 item bonus to attack rolls with the bomb. When the bomb explodes, it deals 2d6 force damage and 2 force splash damage.

Surfaces in the splash area are filled with twisting eddies of force, which are difficult terrain for incorporeal creatures but not for corporeal ones. The force eddies in a square disperse after an incorporeal creature enters the square.

**Source:** `= this.source` (`= this.source-type`)
