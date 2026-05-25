---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Disarm]]", "[[Fatal d8]]", "[[Monk]]"]
price: "{'sp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This punching dagger resembles the standard katar, save that a pair of blades can be folded out from the center blade, transforming the weapon into a starburst shape well suited to catching foes' weapons.

**Source:** `= this.source` (`= this.source-type`)
