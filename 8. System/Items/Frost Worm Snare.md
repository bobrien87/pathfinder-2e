---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Clockwork]]", "[[Cold]]", "[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 115}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The snare takes the form of a Tiny frost worm clockwork toy. When a creature enters its square, the snare activates, causing the worm to let loose a @Template[type:line|distance:30] of frost in the direction from which the creature entered the square. For instance, if a creature entered the square coming from the south, the worm would shoot the line south, to hit any allies of the triggering creature. Those within the line take @Damage[10d6[cold]|options:area-damage] damage with a DC 25 [[Reflex]] save. After spitting its frost, the snare falls apart.

**Source:** `= this.source` (`= this.source-type`)
