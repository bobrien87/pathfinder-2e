---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Clockwork]]", "[[Consumable]]", "[[Fire]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 6}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When a creature enters this snare's square, it triggers an extremely loud clockwork device, which explodes with a bang that can be heard from 200 feet away and deals 1d8 fire damage. The creature must attempt a DC 18 [[Reflex]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is [[Deafened]] for 1 round.
- **Critical Failure** The creature takes double damage and is [[Deafened]] for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
