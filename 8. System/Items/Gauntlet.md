---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Free hand]]"]
price: "{'sp': 2}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A pair of these metal gloves comes with full plate, half plate, and splint armor; they can also be purchased separately and worn with other types of armor. They not only protect your hands but also transform your hands into lethal weapons.

**Source:** `= this.source` (`= this.source-type`)
