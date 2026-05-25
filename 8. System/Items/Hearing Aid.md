---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 5}"
usage: "worn"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A hearing aid is worn in the ear and is made from carved wood, shaped metal, or even small clockwork pieces. The shape of the device aids those that are hard of hearing, and you can wear one or two depending on your hearing loss. You can attach or remove your hearing aids as an Interact action.

**Source:** `= this.source` (`= this.source-type`)
