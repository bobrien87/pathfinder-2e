---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Kickback]]"]
price: "{'gp': 8}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A favored weapon of monster hunters in Arcadia, the harmona gun is a large-bore long gun that fires a heavy, slow-moving round. The gun got its name due to the eerie similarity between the buzzing sound its oversized projectiles make flying through the air and the flight of a fey bird called a harmona.

**Source:** `= this.source` (`= this.source-type`)
