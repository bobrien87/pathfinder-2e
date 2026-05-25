---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 300}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

A material essence disruptor emits bursts of disordered energy to break down the structure of a spell that manipulates material essence. Attempt to counteract an active arcane or primal spell within 60 feet, with a +18 counteract modifier and a counteract rank of 6.

**Source:** `= this.source` (`= this.source-type`)
