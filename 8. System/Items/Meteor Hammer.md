---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Backswing]]", "[[Disarm]]", "[[Reach]]", "[[Trip]]"]
price: "{'gp': 3}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This weapon consists of a long chain connected to a heavy weight at each end. When a wielder swings the weights by the chain, they build momentum and can serve as deadly bludgeons with incredible reach.

**Source:** `= this.source` (`= this.source-type`)
