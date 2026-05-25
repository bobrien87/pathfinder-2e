---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Evil]]", "[[Inhaled]]", "[[Poison]]"]
price: "{'gp': 1500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Fumes from the forges of Hell drain health and strength alike.

**Activate** A (manipulate)

**Saving Throw** DC 36 [[Fortitude]] save

**Onset** 1 round

**Maximum Duration** 6 rounds

**Stage 1** 7d8 poison damage and [[Enfeebled]] 1 (1 round)

**Stage 2** 8d8 poison damage and [[Enfeebled]] 2 (1 round)

**Stage 3** 10d8 poison damage and [[Enfeebled]] 3 (1 round)

**Source:** `= this.source` (`= this.source-type`)
