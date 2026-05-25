---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Contact]]", "[[Poison]]"]
price: "{'gp': 225}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This tacky, hardened sap is harvested from trees infected by fungal blights and exposed to open flames.

**Activate** A (manipulate)

**Saving Throw** DC 30 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 6 rounds

**Stage 1** 6d6 poison damage (1 round)

**Stage 2** 7d6 poison damage (1 round)

**Stage 3** 9d6 poison damage (1 round)

**Source:** `= this.source` (`= this.source-type`)
