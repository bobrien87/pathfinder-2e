---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Magical]]"]
price: "{'gp': 5}"
usage: "worn"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These curved hearing aids hook over the top and sit behind your ear, with a receiver that fits into the ear opening. The external part of the device detects sound waves and, using magic, transfers them down the receiver and into your ear. You can wear one or two depending on your hearing loss, and you can turn your hearing aids on or off using an Interact action.

**Source:** `= this.source` (`= this.source-type`)
