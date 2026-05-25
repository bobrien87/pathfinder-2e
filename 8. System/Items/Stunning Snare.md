---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 320}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You rig a snare to disorient a creature with a quick bash, leaving it with little ability to defend itself. The trap deals 10d6 bludgeoning damage to the first creature to enter its square; that creature must attempt a [[Reflex]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and is [[Off Guard]] for 1 round and [[Stunned]] 1.
- **Failure** The creature takes full damage and is off-guard for 1 round and [[Stunned]] 2.
- **Critical Failure** The creature takes double damage and is off-guard for 1 minute and [[Stunned]] 4.

**Source:** `= this.source` (`= this.source-type`)
