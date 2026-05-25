---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 6}"
bulk: "2"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Also known as "varman" in some parts of the Impossible Lands, this armor is made from fine metal cables woven into latticework patterns with plated segments to protect the head, neck, and shoulders. This armor disperses blows much like rings of chain mail but is much tighter in construction, making it quieter.

**Source:** `= this.source` (`= this.source-type`)
