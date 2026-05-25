---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Deadly d6]]", "[[Finesse]]"]
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

Developed by Alkenstar scouts who often don't have time to break down a [[Tripod]] when beset by the chaotic mutant monsters of the Mana Wastes, this two-pronged stabbing weapon can be used as a bipod to stabilize a gun with potent kickback. A forked bipod can be deployed or retrieved for use as a melee weapon as an Interact action. As with a Tripod, you can change your grip on the weapon as part of this action.

**Source:** `= this.source` (`= this.source-type`)
