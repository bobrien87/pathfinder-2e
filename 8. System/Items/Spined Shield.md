---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]"]
price: "{'gp': 360}"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Five jagged spines project from the surface of this steel shield (Hardness 6, HP 24, BT 12). The spines are +1 striking shield spikes.

When you use the Shield Block reaction with this shield, the spines take the damage before the shield itself does. When the shield would take damage (after applying Hardness), one spine snaps off per 6 damage, reducing the damage by 6. The shield takes any remaining damage. When there are no spines left, the shield takes damage as normal.

When all the spines are gone, you lose the ability to attack with them until the spines regenerate the next day.

> [!danger] Effect: Spined Shield Spines

**Activate** A Interact

**Effect** You shoot one of the shield's spines at a target. A fired spine uses the spikes' statistics, but it is a martial ranged weapon with a range increment of 120 feet.

**Source:** `= this.source` (`= this.source-type`)
