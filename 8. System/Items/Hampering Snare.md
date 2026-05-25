---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You arrange brambles, wires, sticky goo, or other materials to interfere with a creature's movement. The square with this snare, as well as three adjacent squares (to form a @Template[square|distance:10]{10-foot-by-10-foot area}), become difficult terrain when the first creature enters the snare's square. The difficult terrain affects the creature's movement right away, including its movement into the triggering square, and it lasts for 1d4 rounds after the snare is triggered. A creature can use an Interact action to clear the difficult terrain out of a single square early.

**Source:** `= this.source` (`= this.source-type`)
