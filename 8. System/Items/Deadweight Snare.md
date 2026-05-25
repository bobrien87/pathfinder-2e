---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Kobold]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 6}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This snare is made of magnetized weights and heavy ropes rigged to a trip wire or pressure plate. When a creature enters the square, the magnets and ropes deploy, weighing down the creature's weapons and limbs. The creature must attempt a [[Reflex]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes a -1 status penalty to attack rolls for 1 round or until it Escapes.

> [!danger] Effect: Deadweight Snare (Success)
- **Failure** The creature takes a -2 status penalty to attack rolls for 1 minute or until it Escapes (DC 18).
- **Critical Failure** As failure, but the creature drops any metallic items it's holding.

> [!danger] Effect: Deadweight Snare (Failure/Critical Failure)

**Source:** `= this.source` (`= this.source-type`)
