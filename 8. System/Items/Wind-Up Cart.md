---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Clockwork]]", "[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 6}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This primitive device can be cobbled together from springs, wheels, and scrap and is commonly used to carry rocks or other dead weight forward to trigger traps. It can be loaded with up to 4 Bulk of items. Most creatures aren't small enough to fit on the cart, and even for Tiny creatures, it makes for a choppy ride; while riding the cart, a creature gains two actions at the start of each of its turns, instead of three. Once activated, the cart moves forward at a speed of 30 feet per round on your turn for up to 1 minute. If it strikes an obstruction, it attempts to continue its movement, pushing with an Athletics bonus of +5, once per round. The wind-up cart has AC 15, Hardness 2, 24 Hit Points, and a Break Threshold of 12. After its 1-minute duration completes, the cart collapses back into scrap.

**Source:** `= this.source` (`= this.source-type`)
