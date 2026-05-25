---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Companion]]", "[[Invested]]", "[[Primal]]"]
price: "{'gp': 4250}"
usage: "wornhorseshoes"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When you affix these simple iron horseshoes to the hooves of an ordinary horse or a quadrupedal animal companion and the animal companion invests them, that creature gains a +10-foot item bonus to its land Speed and a +3 item bonus to Athletics checks to High Jump and Long Jump.

In addition, when it Leaps, it can move 5 feet farther if jumping horizontally or 3 feet higher if jumping vertically.

**Source:** `= this.source` (`= this.source-type`)
