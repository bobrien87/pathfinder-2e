---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Kobold]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 700}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Sharp metal jaws wind tightly into the pressure plate mechanism of this snare. When triggered, the jaws clamp shut and spin, damaging limbs in the process. The snare deals 10d8 piercing damage to the first creature to enter the square; that creature must attempt a DC 34 [[Reflex]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and is [[Off Guard]] until the end of its next turn.
- **Failure** The creature takes full damage plus 2d6 bleed, and it becomes [[Clumsy]] 2 for 1 round.
- **Critical Failure** The creature takes double damage plus 4d6 bleed, and it becomes [[Clumsy]] 2 for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
