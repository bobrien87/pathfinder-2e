---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 700}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This snare uses tightly wound springs, clockwork, and shrapnel to cause devastating damage. When a creature enters the snare's square, the trap releases, dealing 12d6 piercing damage in a deafening explosion. Everyone in a @Template[emanation|distance:10]{10-foot radius} of the snare's square must attempt a DC 31 [[Reflex]] save.
- **Critical Success** The creature in unaffected,
- **Success** The creature takes half damage and is [[Deafened]] for 1 round.
- **Failure** The creature takes full damage, 2d6 persistent,piercing damage, and is [[Deafened]] for 1 minute.
- **Critical Failure** The creature takes double damage, 4d6 persistent,piercing damage, and is [[Deafened]] for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
