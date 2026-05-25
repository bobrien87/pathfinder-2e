---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Combination]]", "[[Concussive]]", "[[Fatal d8]]", "[[Monk]]"]
price: "{'gp': 8}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This pair of knuckle dusters is fitted with an explosive charge of black powder within the hollowed spikes of the weapon and a firing mechanism you hold in your hand while in use.

**Source:** `= this.source` (`= this.source-type`)
