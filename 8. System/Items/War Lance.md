---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Deadly d8]]", "[[Jousting d6]]", "[[Parry]]", "[[Shove]]"]
price: "{'gp': 4}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This lance appears shorter and stockier in comparison to other weapons of its type. The war lance notably features shielding integrated into its vamplate, exchanging its reach for a sturdier base when defending against attacks or attempting to overpower an opponent.

**Source:** `= this.source` (`= this.source-type`)
