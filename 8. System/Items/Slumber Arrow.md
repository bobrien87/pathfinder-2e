---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]", "[[Mental]]", "[[Sleep]]"]
price: "{'gp': 11}"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

Sleep arrows often have shafts of deep blue or black, and their fletching is exceptionally soft and downy. An activated sleep arrow deals no damage, but a living creature hit by it grows lethargic and must attempt a DC 17 [[Will]] save saving throw. On a failure, it takes a –5-foot status penalty to its Speeds for 1 round, and is also [[Slowed]] 1 for 1 round on a critical failure.

**Craft Requirements** Supply one casting of *sleep*.

**Source:** `= this.source` (`= this.source-type`)
