---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Clockwork]]", "[[Mechanical]]"]
price: "{'gp': 150}"
usage: "worn"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Fitted into each of these prosthetic legs is a large spring, tightly bound around a collapsible shaft. When released, the spring unspools rapidly and the shaft telescopes out and back, returning to its compressed form and catapulting you forward.

**Activate** `pf2:1` (concentrate, manipulate)

**Frequency** once per hour

**Effect** You Stride up to twice your speed or [[Leap]] up to 20 feet horizontally and 5 feet vertically.

**Source:** `= this.source` (`= this.source-type`)
