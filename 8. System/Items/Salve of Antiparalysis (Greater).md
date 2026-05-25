---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Healing]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 325}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Applying this filmy salve to a creature helps it overcome magical paralysis. If the creature is petrified, it returns to normal, and for removing paralysis, the salve's counteract modifier is +31 and its counteract rank is 6th.

**Source:** `= this.source` (`= this.source-type`)
