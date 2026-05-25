---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Razing]]", "[[Shove]]", "[[Sweep]]"]
price: "{'gp': 3}"
usage: "held-in-two-hands"
bulk: "3"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The tetsubo is a war club constructed out of heavy wood shod with iron studs, designed for smashing through armor and defenses. A tetsubo made entirely out of metal might also be referred to as a kanabo.

**Source:** `= this.source` (`= this.source-type`)
