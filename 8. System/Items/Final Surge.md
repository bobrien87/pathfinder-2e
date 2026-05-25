---
type: item
source-type: "Remaster"
level: "1"
traits: ""
price: ""
usage: ""
bulk: "—"
activate: ""
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null, "**Traits** " + this.traits, "")`

`= choice(this.price != null, "**Price** " + this.price, "") + choice(this.usage != null, choice(this.price != null, "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null, choice(this.price != null or this.usage != null, "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null, "**Activate** " + this.activate, "")`

You Stride twice. The Drakeheart Mutagen's duration ends.

**Source:** `= this.source` (`= this.source-type`)
