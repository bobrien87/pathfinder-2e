---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Acid]]", "[[Clockwork]]", "[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 15}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This tin clockwork lizard is activated when a creature moves adjacent to it, at which point it spits out a glob of acid. The target must succeed at a DC 20 [[Reflex]] save saving throw or take 3d6 acid damage.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes full damage.
- **Failure** The creature takes full damage and 5 persistent,acid damage.
- **Critical Failure** The creature takes double damage and 10 persistent,acid damage.

**Source:** `= this.source` (`= this.source-type`)
