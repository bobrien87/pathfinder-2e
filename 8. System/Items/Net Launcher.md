---
type: item
source-type: "Remaster"
level: "1"
price: "{'gp': 16}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wide, hollow tube is two to three feet long and fires an unattached net at much greater range than one can be thrown. A net launcher can be wielded while propped up on your shoulder or cradled under your arm. A net must be carefully folded to be launched without tangling. Properly loading a net into a net launcher takes 1 minute. A net fired with a net launcher can target a Medium or smaller creature within 40 feet, rather than 20 feet.

**Source:** `= this.source` (`= this.source-type`)
