---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Agile]]", "[[Finesse]]", "[[Kobold]]", "[[Ranged trip]]", "[[Tethered]]", "[[Thrown 10]]", "[[Trip]]"]
price: "{'gp': 6}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This weapon consists of a three-pronged barbed hook attached to a length of chain. It can be used in melee to stab foes or hurled at a range. Some kobolds are particularly fond of using flying talons, especially as a sort of badge of office above those who serve them.

**Source:** `= this.source` (`= this.source-type`)
