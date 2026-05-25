---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]", "[[Snare]]", "[[Trap]]", "[[Water]]"]
price: "{'gp': 40}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This snare magically contains a pressurized jet of water activated by an invisible sensor. When a creature enters the snare's square, a powerful blast of water deals 4d10 bludgeoning damage to the creature and potentially pushes them. You determine the direction of the blast of water when crafting the snare. The triggering creature must attempt a DC 24 [[Fortitude]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is pushed 10 feet in the determined direction.
- **Critical Failure** The creature takes double damage, is pushed 15 feet in the determined direction, and is drenched with water, taking a –1 circumstance penalty to saving throws against electricity effects for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
