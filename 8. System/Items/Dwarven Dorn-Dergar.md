---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Dwarf]]", "[[Razing]]", "[[Reach]]"]
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

A heavy, weighted cube of metal at the end of a long chain, the dorn-dergar is used by dwarven berserkers and sappers who specialize in breaking through lines of shielded opponents or disabling enemy siege weapons.

**Source:** `= this.source` (`= this.source-type`)
