---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Nonlethal]]"]
price: "{'sp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A sap has a soft wrapping around a dense core, typically a leather sheath around a lead rod. Its head is wider than its grip to disperse the force of a blow, as the weapon's purpose is to knock out its victim rather than to draw blood.

**Source:** `= this.source` (`= this.source-type`)
