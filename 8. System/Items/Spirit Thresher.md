---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Kholo]]", "[[Sweep]]", "[[Versatile s]]"]
price: "{'gp': 2}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Bones, some solid and others splintered, are affixed to metal chains at the end of a long stick to form a powerful flail. Many kholo warriors insist the vicious crack the weapon makes as it strikes loosens fragments of the soul like husks struck from grains.

**Source:** `= this.source` (`= this.source-type`)
