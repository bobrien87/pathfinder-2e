---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Free hand]]", "[[Monk]]"]
price: "{'sp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This bit of hardened metal, favored by street toughs, is typically made of brass and features four finger holes so that it can sit atop the knuckles, adding extra power to a punch.

**Source:** `= this.source` (`= this.source-type`)
