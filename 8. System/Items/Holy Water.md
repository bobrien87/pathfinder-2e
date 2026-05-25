---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Divine]]", "[[Holy]]", "[[Splash]]", "[[Thrown]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A Strike

This vial contains water blessed by a benevolent deity. You activate a vial of *holy water* by throwing it as a Strike. It's a simple thrown weapon with a range increment of 20 feet.

*Holy water* deals 1d6 spirit damage and 1 spirit splash damage. *Holy water* can damage only creatures with the unholy trait.

**Source:** `= this.source` (`= this.source-type`)
