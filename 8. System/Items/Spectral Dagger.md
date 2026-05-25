---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Finesse]]", "[[Thrown 10]]", "[[Versatile s]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Granted by [[Spectral Dagger]]

**Source:** `= this.source` (`= this.source-type`)
