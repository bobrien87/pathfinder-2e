---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Repeating]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This handheld crossbow features an ingeniously designed catch mechanism at the top of the flight groove, just in front of the latch, which automatically loads a bolt from a magazine and resets the string each time the weapon is fired. A typical repeating hand crossbow magazine holds five bolts.

**Source:** `= this.source` (`= this.source-type`)
