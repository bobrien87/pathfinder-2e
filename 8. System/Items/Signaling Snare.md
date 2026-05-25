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

A subtle snare used in hunting or tracking, a signaling snare often consists of carefully prepared earth, piled sand or stones, specific arrangements of vegetation, and so forth. When a creature enters a square of a signaling snare, nothing happens to the creature, but instead it causes a small, unobtrusive disruption to the terrain that allows the snare's creator or another creature who knows what to look for to determine whether a creature of the appropriate size entered the square.

**Source:** `= this.source` (`= this.source-type`)
