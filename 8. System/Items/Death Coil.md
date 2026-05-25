---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Consumable]]", "[[Electricity]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 9000}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This modified Stasian coil of metal and glass stands about three feet tall. It activates when at least three creatures are within 20 feet of it, or if at least one creature stays within 20 feet of it for more than 1 round. It then lashes out with a torrent of electrical energy dealing 7d12 electricity damage to all creatures within 20 feet of it. Due to the fact that it doesn't trigger immediately when a creature enters its square, abilities like [[Surprise Snare]] don't work with a death coil. Creatures within that area must attempt a DC 43 [[Fortitude]] save saving throw.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is [[Stunned]] 2.
- **Critical Failure** The creature takes double damage is [[Stunned]] 4.

**Source:** `= this.source` (`= this.source-type`)
