---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Clockwork]]"]
price: "{'gp': 2}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This extendable rod features a pincer on one end and clamped handle on the other. By squeezing the handle, the pincer opens or closes. As an Interact action, you can extend or retract the rod by 5 feet to one of three settings, allowing you to Interact to pick up an object with the pincer either within your own space, in an adjacent space, or exactly 10 feet away.

**Source:** `= this.source` (`= this.source-type`)
