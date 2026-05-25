---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Disarm]]", "[[Finesse]]", "[[Tengu]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This fan-shaped sword designed by tengu smiths has five broad blades that join at its hilt. Tengu sailors use them as makeshift weather vanes, for the sword spins in the wind's direction when loosely held aloft.

**Source:** `= this.source` (`= this.source-type`)
