---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Laminar]]"]
price: "{'gp': 5}"
bulk: "1"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Sankeit is common armor among Varki in the northern Land of the Linnorm Kings, made of small wooden plates or longer slats, typically vertical, joined with sinew or cord and painted with decorations. Varki warriors traditionally wear sankeit with a fearsome wooden helm carved in the shape of a mighty creature.

**Source:** `= this.source` (`= this.source-type`)
