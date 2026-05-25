---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Concealable]]", "[[Finesse]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This slender, rapier-like sword is concealed within a wooden or metal cane that serves as a sheath, making it an inconspicuous weapon easy to slip past inspections or into high-society events. A sword cane is typically 4 feet long when sheathed, and its hilt is usually capped with a wooden or metal decoration.

**Source:** `= this.source` (`= this.source-type`)
