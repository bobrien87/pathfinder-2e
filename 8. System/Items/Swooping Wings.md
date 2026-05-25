---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "implanted"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A pair of feathered wings are anchored to your shoulder bones. You gain a 25-foot fly Speed.

**Source:** `= this.source` (`= this.source-type`)
