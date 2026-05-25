---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 2}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This sturdy pole has a rope attached to one end in a loop with the other end extending to the handle. You can pull the handle side of the rope to tighten the loop. Using this loop, you can [[Grapple]] without having a free hand. A creature grabbed this way receives a –2 circumstance penalty to attack rolls when Striking with an unarmed attack. Due to limitations in the size of the loop, a catch pole can only be used on creatures sized Medium or smaller.

> [!danger] Effect: Catch Pole

**Source:** `= this.source` (`= this.source-type`)
