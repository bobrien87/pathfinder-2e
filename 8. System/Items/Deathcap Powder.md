---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 450}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The toxic deathcap mushroom can be dried, ground, and treated to form a flavorless powder with accelerated effects.

**Activate** A (manipulate)

**Saving Throw** DC 33 [[Fortitude]] save

**Onset** 10 minutes

**Maximum Duration** 6 minutes

**Stage 1** 7d8 poison damage (1 minute)

**Stage 2** 9d6 poison damage and [[Sickened]] 2 (1 minute)

**Stage 3** 8d10 poison damage and [[Sickened]] 3 (1 minute)

**Source:** `= this.source` (`= this.source-type`)
