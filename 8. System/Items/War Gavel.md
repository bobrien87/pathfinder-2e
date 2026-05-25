---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Versatile p]]"]
price: "{'sp': 2}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A war gavel is similar in construction to a palstave axe, but instead of inserting a metal wedge, it uses a heavier wooden head that is either carved into several points or inset with pointed objects like the teeth of large mammals.

**Source:** `= this.source` (`= this.source-type`)
