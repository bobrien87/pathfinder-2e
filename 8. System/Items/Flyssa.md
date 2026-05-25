---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Finesse]]", "[[Versatile p]]"]
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

This single-edged blade has a guardless hilt. Often decorated with elaborate etchings, a flyssa is longer than most daggers but shorter than average for most swords, making it useful in close and pitched combat.

**Source:** `= this.source` (`= this.source-type`)
