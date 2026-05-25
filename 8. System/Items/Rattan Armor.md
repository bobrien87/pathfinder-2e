---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Aquadynamic]]"]
price: "{'gp': 2}"
bulk: "1"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This armor is made from rattan reeds which are bent and woven into shaped layers then treated with oil to harden them. Due to the materials and nature of its construction, rattan armor is naturally buoyant and doesn't hinder its wearer when moving through water.

**Source:** `= this.source` (`= this.source-type`)
