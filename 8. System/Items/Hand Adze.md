---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Finesse]]", "[[Sweep]]", "[[Thrown 10]]", "[[Tripkee]]"]
price: "{'sp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The adze's smaller version is useful for delicate woodworking in cramped spaces. Tripkees use hand adzes for crafting and as close quarters weapons.

**Source:** `= this.source` (`= this.source-type`)
