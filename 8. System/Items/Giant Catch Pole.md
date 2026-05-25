---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 50}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This sturdy pole has a rope attached to one end in a loop with the other end extending to the handle. You can pull the handle side of the rope to tighten the loop. Using this loop, you can [[Grapple]] without having a free hand. A creature grabbed this way receives a –2 circumstance penalty to attack rolls when Striking with an unarmed attack. Due to limitations in the size of the loop, a catch pole can only be used on creatures sized Medium or smaller.

A giant catch pole is made from thicker steel and heavier rope. It functions the same as a catch pole but can be used to Grapple creatures up to your normal size limit. However, the implement is so ungainly that you are [[Clumsy]] 1 while wielding it.

> [!danger] Effect: Catch Pole

**Source:** `= this.source` (`= this.source-type`)
