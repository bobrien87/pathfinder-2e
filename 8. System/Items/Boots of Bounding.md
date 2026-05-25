---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 340}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The springy soles of these sturdy leather boots cushion your feet and make each step lighter. These boots give you a +5-foot item bonus to your Speed and a +2 item bonus to Athletics checks to High Jump and Long Jump.

In addition, when you use the Leap action, you can move 5 feet further if jumping horizontally or 3 feet higher if jumping vertically.

**Source:** `= this.source` (`= this.source-type`)
