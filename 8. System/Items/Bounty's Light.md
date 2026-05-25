---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Fire]]", "[[Magical]]", "[[Relic]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magical torch that's made up of a bouquet of living summer flowers functions as a *[[Staff of Fire (Greater)]]*. Its light turns on and off with an Interact action.

**Source:** `= this.source` (`= this.source-type`)
