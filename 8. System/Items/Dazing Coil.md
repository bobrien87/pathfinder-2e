---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 900}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You deal damage to an [[Off Guard]] creature with the affixed weapon

This knot of copper wire reshapes itself in a new pattern every time its affixed weapon deals damage. When you activate the coil, the damaged creature must succeed at a DC 31 [[Will]] save or be [[Stunned]] 1. If it critically fails, it instead becomes [[Stunned]] 2.

**Source:** `= this.source` (`= this.source-type`)
