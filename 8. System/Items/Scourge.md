---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Disarm]]", "[[Finesse]]", "[[Nonlethal]]", "[[Sweep]]"]
price: "{'sp': 1}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A scourge—also known as a cat-o'-nine-tails—is a set of several knotted cords made from cotton or leather and attached to a handle. While most scourges are more suitable for torture than combat, when fashioned into a weapon, a scourge can have metal barbs woven into the cords to pierce clothing and armor.

**Source:** `= this.source` (`= this.source-type`)
