---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Fatal d10]]"]
price: "{'gp': 3}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This amazingly simple projectile weapon is nothing more than a metal tube packed with black powder and a stopper, attached to the sharpened head of a javelin. A loaded fire lance can be wielded as a normal spear, though it requires an Interact action to regrip the weapon and hold it properly when switching from one use to another. Fire lances are most commonly found in Tian Xia, though occasionally one makes its way all the way to Avistan, typically in the hands of a Tien mercenary or caravan guard.

**Source:** `= this.source` (`= this.source-type`)
