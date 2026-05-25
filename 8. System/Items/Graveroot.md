---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The opaque white sap from the graveroot shrub clouds the mind.

**Activate** `pf2:2` (manipulate)

**Saving Throw** DC 19 [[Fortitude]] save

**Maximum Duration** 4 rounds

**Stage 1** 1d8 poison damage (1 round)

**Stage 2** 1d10 poison damage and [[Stupefied 1]] (1 round)

**Stage 3** 2d6 poison damage and [[Stupefied 2]] (1 round)

**Source:** `= this.source` (`= this.source-type`)
