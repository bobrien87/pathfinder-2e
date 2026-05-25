---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Contact]]", "[[Poison]]", "[[Virulent]]"]
price: "{'gp': 12000}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Tears of death are among the most powerful of alchemical poisons, distilled from extracts of five other deadly poisons in just the right ratios.

**Activate** A (manipulate)

**Saving Throw** DC 44 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 10 minutes

**Stage 1** 20d6 poison damage and [[Paralyzed]] (1 round)

**Stage 2** 22d6 poison damage and [[Paralyzed]] (1 minute)

**Stage 3** 24d6 poison damage and [[Paralyzed]] (1 minute)

**Source:** `= this.source` (`= this.source-type`)
