---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Tethered]]", "[[Thrown 30]]"]
price: "{'gp': 1}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A war javelin is similar to a standard javelin, but made of sturdier woods with additional leather grips to make it suitable as a melee weapon and a leather thong to retrieve it after it's thrown.

**Source:** `= this.source` (`= this.source-type`)
