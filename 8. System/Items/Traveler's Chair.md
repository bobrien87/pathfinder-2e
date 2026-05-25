---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 5}"
usage: "worn"
bulk: "3"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A traveler's chair is tailored for frequent adventures and travels. The design is sleek and fashionable to provide excellent comfort and support. A traveler's chair has small mechanisms, either made from interlocking wood pieces, clockwork, or other devices, that allow the chair to traverse up or down stairs without any additional difficulty (moving up stairs is still difficult terrain, just like for other characters), and move through other common adventuring terrain without any additional difficulty, such as ladders and uneven ground.

**Source:** `= this.source` (`= this.source-type`)
