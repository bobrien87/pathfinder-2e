---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Combination]]", "[[Dwarf]]", "[[Ranged trip]]", "[[Razing]]"]
price: "{'gp': 8}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The wrecker combines a dwarven dorn-dergar with a heavy, gear-reinforced arm cover that allows it to be fired like an oversized sling, then retrieved and reloaded by manually activating a clockwork spool. A wrecker must be loaded to be switched from its ranged configuration to its melee configuration.

**Source:** `= this.source` (`= this.source-type`)
