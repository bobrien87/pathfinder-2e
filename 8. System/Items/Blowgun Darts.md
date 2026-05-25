---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Consumable]]"]
price: "{'cp': 5}"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These thin, light darts are typically made of hardwood and stabilized with fletching of down or fur. They are often hollow so they can be used to deliver poison.

**Source:** `= this.source` (`= this.source-type`)
