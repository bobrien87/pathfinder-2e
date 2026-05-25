---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Auditory]]", "[[Clockwork]]", "[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 12}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This snare uses clockwork stressed almost to the breaking point, which activates with a powerful explosion that deals 3d8 piercing damage to the first creature entering the snare's square. The creature must attempt a DC 19 [[Reflex]] save saving throw.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and 3 bleed damage.
- **Critical Failure** The creature takes double damage and 6 bleed damage.

**Source:** `= this.source` (`= this.source-type`)
