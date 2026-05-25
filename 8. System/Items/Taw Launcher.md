---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Conrasu]]", "[[Deadly d10]]", "[[Modular]]"]
price: "{'gp': 10}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This complex device is a crossbow and fires small wooden bullets known as taws. A system of blades within the launcher can rapidly reshape a taw as it's loaded, allowing the launcher to fire taws of different shapes, such as fléchettes.

**Source:** `= this.source` (`= this.source-type`)
