---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 1}"
usage: "worn"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This leather bandolier holds up to three magazines for repeating weapons in leather pockets that pop open with the quick flick of a thumb. You can replace a magazine in a repeating weapon with a magazine from a worn bandolier faster, reducing the number of Interact actions required by 1. You can wear only one repeater bandolier at a time.

**Source:** `= this.source` (`= this.source-type`)
