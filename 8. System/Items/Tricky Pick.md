---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Backstabber]]", "[[Fatal d10]]", "[[Kobold]]", "[[Modular]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ingenious kobold pick conceals several hidden traps that the wielder can activate to trick and befuddle foes with a variety of damaging blades and bludgeoning surfaces.

**Source:** `= this.source` (`= this.source-type`)
