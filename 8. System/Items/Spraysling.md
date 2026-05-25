---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Halfling]]", "[[Propulsive]]", "[[Scatter 5]]"]
price: "{'gp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A spraysling is similar to a standard sling but with a wider cup fitted with a thin blade affixed to the cup's edges. When used to make an attack with a specially prepared packet of spray pellets, the razor slices open the packet and the weapon launches a cluster of stinging pellets.

**Source:** `= this.source` (`= this.source-type`)
