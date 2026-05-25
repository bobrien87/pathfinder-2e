---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Concussive]]", "[[Double barrel]]", "[[Fatal d8]]"]
price: "{'gp': 6}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This flintlock pistol has two side-by-side barrels. Though less accurate than a standard pistol, a double-barreled pistol is a useful and versatile weapon. It's generally banned in areas where duels with pistols are relatively common, in much the same way that arriving at an aristocratic duel with a scattergun would be considered crass, at best.

**Source:** `= this.source` (`= this.source-type`)
