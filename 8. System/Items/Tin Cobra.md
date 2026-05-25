---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Clockwork]]", "[[Consumable]]", "[[Mechanical]]", "[[Poison]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 23}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This clockwork cobra activates when a creature enters its square, at which point it lashes out and spits venom, dealing 3d6 poison damage. The target must attempt a DC 21 [[Fortitude]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is [[Sickened]] 1.
- **Critical Failure** The creature takes double damage is [[Sickened]] 2.

**Source:** `= this.source` (`= this.source-type`)
