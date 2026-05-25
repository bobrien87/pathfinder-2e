---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 330}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Thanks to a graft from a hardy deep-sea invertebrate in your stomach, you can ingest food and water that would be toxic to others. You gain a +2 item bonus to Fortitude saving throws against ingested diseases and poisons.

**Source:** `= this.source` (`= this.source-type`)
