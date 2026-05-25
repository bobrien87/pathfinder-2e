---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Catfolk]]", "[[Finesse]]", "[[Hampering]]", "[[Reach]]"]
price: "{'gp': 5}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The whip claw is a long tether affixed to claw-like daggers, allowing the wielder to fling and retract them with deadly precision. Catfolk first developed this weapon to provide extended reach when hunting dangerous animals, and they wield them with unmatched expertise.

**Source:** `= this.source` (`= this.source-type`)
