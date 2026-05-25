---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Concussive]]", "[[Fatal d8]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Though less accurate and powerful than a flintlock musket, the flintlock pistol is a preferred weapon of privateers thanks to its more compact size and affordability. Pirate captains often wear a brace of such pistols in a bandolier so they can draw and fire without stopping to reload.

**Source:** `= this.source` (`= this.source-type`)
