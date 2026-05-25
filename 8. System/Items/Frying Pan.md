---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Fatal d8]]", "[[Halfling]]"]
price: "{'sp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The cast-iron frying pan is an essential tool for adventuring halflings, gold panners, and remote tavern owners. Characters with the [[Halfling Weapon Familiarity]] ancestry feat are trained in the frying pan.

**Source:** `= this.source` (`= this.source-type`)
