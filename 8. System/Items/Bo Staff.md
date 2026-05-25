---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Monk]]", "[[Parry]]", "[[Reach]]", "[[Trip]]"]
price: "{'sp': 2}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This strong but slender staff is tapered at the ends and well balanced. It's designed to be an offensive and defensive weapon.

**Source:** `= this.source` (`= this.source-type`)
