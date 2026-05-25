---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 1}"
usage: "affixed-to-a-creature"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Small and unobtrusive tags made from a durable material, often leather or hardwood, tracking tags are attached to wild animals, usually by a collar, to track their movements. They also serve as a way to let others know that someone is keeping track of this animal. Each tag is also inscribed with a unique label so individual creatures can be more easily identified among a herd.

**Source:** `= this.source` (`= this.source-type`)
