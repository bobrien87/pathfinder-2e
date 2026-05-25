---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 1000}"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

With a superior design and excellent craftsmanship, this steel shield has higher Hardness than its non-magical counterparts, making it harder to break and destroy.

The shield has Hardness 13, HP 104, and BT 52.

**Source:** `= this.source` (`= this.source-type`)
