---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Foldaway]]"]
price: "{'gp': 5}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This buckler-sized shield is segmented, allowing it to collapse into a housing bound to a gauntlet for easy storage. A small catch enables you to expand the shield quickly in battle when you're in need of defense.

**Source:** `= this.source` (`= this.source-type`)
