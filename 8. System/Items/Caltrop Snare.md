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

This snare consists of a hidden canister of [[Caltrops]] attached to a trip wire. When the snare is triggered, it flings the caltrops into either the snare's square or a square adjacent to the snare. You choose which square when you set up the snare.

If the caltrops scatter into the same square as a creature, that creature must attempt the Acrobatics check immediately.

**Craft Requirements** Supply a container of caltrops.

**Source:** `= this.source` (`= this.source-type`)
