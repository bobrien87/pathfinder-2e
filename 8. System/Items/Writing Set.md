---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 1}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Using a writing set, you can draft correspondence and scribe scrolls. A set includes stationery, including a variety of paper and parchment, as well as ink, a quill or inkpen, sealing wax, and a simple seal. If you've written a large amount, you can refill your kit with extra ink and paper.

**Source:** `= this.source` (`= this.source-type`)
