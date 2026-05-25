---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Flexible]]", "[[Noisy]]"]
price: "{'gp': 5}"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Sometimes called a hauberk, this is a long shirt constructed of the same metal rings as chain mail. However, it is much lighter than chain mail and protects only the torso, upper arms, and upper legs of its wearer.

**Source:** `= this.source` (`= this.source-type`)
