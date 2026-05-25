---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Monk]]", "[[Trip]]"]
price: "{'gp': 2}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This heavy blade is favored by guardians of religious sites. It has a distinctive, crescent-shaped blade that seems to be a mix of a sickle and sword. It often has holes drilled into the blade or the pommel so that bells or other holy trinkets can be affixed to the weapon.

**Source:** `= this.source` (`= this.source-type`)
