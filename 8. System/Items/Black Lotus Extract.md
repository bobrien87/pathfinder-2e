---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Contact]]", "[[Poison]]", "[[Virulent]]"]
price: "{'gp': 6500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Black lotus extract causes severe internal bleeding.

**Activate** A (manipulate)

**Saving Throw** DC 42 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 6 rounds

**Stage 1** 13d6 poison damage and [[Drained]] 1 (1 round)

**Stage 2** 15d6 poison damage and [[Drained]] 1 (1 round)

**Stage 3** 17d6 poison damage and [[Drained]] 2 (1 round)

**Source:** `= this.source` (`= this.source-type`)
