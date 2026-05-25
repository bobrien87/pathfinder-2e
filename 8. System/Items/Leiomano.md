---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Fatal d10]]", "[[Versatile s]]"]
price: "{'gp': 2}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This thick club is inset with sharp teeth, typically from a shark, that easily tear flesh. It's the preferred weapon of many Minatan warriors.

**Source:** `= this.source` (`= this.source-type`)
