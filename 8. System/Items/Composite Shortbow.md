---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Deadly d10]]", "[[Propulsive]]"]
price: "{'gp': 14}"
usage: "held-in-one-plus-hands"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This shortbow is made from horn, wood, and sinew laminated together to increase the power of its pull and the force of its projectile. Its compact size and power make it a favorite of mounted archers. Any time an ability is specifically restricted to a shortbow, it also applies to composite shortbows unless otherwise stated.

**Source:** `= this.source` (`= this.source-type`)
