---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 110}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

This carefully concocted mixture of fungal spores and ground bones has paralytic properties that make it a valuable poison.

**Saving Throw** DC 28 [[Fortitude]] save

**Onset** 10 minutes

**Maximum Duration** 6 minutes

**Stage 1** [[Fatigued]] (1 minute)

**Stage 2** 5d6 poison damage and fatigued (1 minute)

**Stage 3** 5d6 poison damage, fatigued, and [[Paralyzed]] (1 minute)

**Source:** `= this.source` (`= this.source-type`)
