---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 645}"
usage: "wornarmbands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Skilled awl work has imprinted images of a muscled weightlifter into these tiered leather bands, which grant you enhanced stamina and skill when performing athletic exercises.

While fastened to your upper arms, the armbands give you a +2 item bonus to Athletics checks.

In addition, whenever you use an action to Climb or Swim and you succeed at the Athletics check, add a +5-foot item bonus to the distance you move.

**Source:** `= this.source` (`= this.source-type`)
