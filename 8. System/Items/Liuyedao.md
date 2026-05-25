---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Deadly d4]]", "[[Finesse]]", "[[Sweep]]", "[[Versatile p]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The liuyedao, or willow-leaf saber, is a common, one-handed military saber with a moderately curved blade designed for slashing and chopping attacks.

**Source:** `= this.source` (`= this.source-type`)
