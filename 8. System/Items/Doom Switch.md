---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This short length of wood is decorated with fine carvings of symbols representing fate.

**Activate—Bragging Rights** `pf2:1` (attack, manipulate)

**Frequency** once per day

**Effect** You attempt to Strike a significant enemy with the doom switch, marking them for defeat. The switch is treated as a simple melee weapon for the purpose of proficiency. This attack deals no damage.
- **Critical Success** You and your allies gain a +1 status bonus to attack rolls against the target for 1 minute. If you reduce the target to 0 Hit Points during this time, you gain temporary Hit Points equal to twice the target's level for 1 round.
- **Success** As critical success, except you gain temporary Hit Points equal to the target's level.
- **Failure** You and your allies take a –1 status penalty to attack rolls against the target for 1 round.
- **Critical Failure** You and your allies take a –2 status penalty to attack rolls against the target for 1 round.

> [!danger] Effect: Bragging Rights (Success or Better)

> [!danger] Effect: Bragging Rights (Failure or Worse)

**Source:** `= this.source` (`= this.source-type`)
