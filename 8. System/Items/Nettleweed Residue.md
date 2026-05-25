---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Contact]]", "[[Poison]]"]
price: "{'gp': 75}"
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

Concentrated sap of stinging weeds makes an effective toxin.

**Saving Throw** DC 27 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 6 minutes

**Stage 1** 3d6 poison damage (1 minute)

**Stage 2** 4d6 poison damage (1 minute)

**Stage 3** 6d6 poison damage (1 minute)

**Source:** `= this.source` (`= this.source-type`)
