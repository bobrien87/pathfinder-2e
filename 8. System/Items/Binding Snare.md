---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 160}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When a creature enters the snare's square, several strands of strong wires ending in jagged hooks latch onto it before hauling it to the ground. The snare deals 2d6 piercing damage, and the targeted creature must attempt a [[Reflex]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is knocked [[Prone]] and [[Immobilized]] for 1 round (`act escape show-dc=all dc=28`).
- **Critical Failure** The creature takes double damage, is knocked prone, and is [[Restrained]] for 1 round (Escape DC 28).

**Source:** `= this.source` (`= this.source-type`)
