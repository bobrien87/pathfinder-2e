---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A formula book holds the formulas necessary to make items other than the common equipment from Pathfinder Player Core; characters of the alchemist class typically get one for free. Each formula book can hold the formulas for up to 100 different items. Formulas can also appear on parchment sheets, tablets, and almost any other medium; there's no need for you to copy them into a specific book as long as you can keep them on hand to reference them.

**Source:** `= this.source` (`= this.source-type`)
