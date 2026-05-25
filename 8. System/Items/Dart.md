---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Thrown]]"]
price: "{'cp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This thrown weapon is larger than an arrow but shorter than a javelin. It typically has a short shaft of wood ending in a metal tip and is sometimes stabilized by feathers or fur.

**Source:** `= this.source` (`= this.source-type`)
