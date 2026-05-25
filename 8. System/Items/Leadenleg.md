---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 15}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

Once injected, this synthetic toxin sinks into the extremities, numbing them nearly to paralysis.

**Saving Throw** DC 20 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 1d10 poison damage and –5-foot status penalty to all Speeds (1 round)

**Stage 2** 2d6 poison damage and –10-foot status penalty to all Speeds (1 round)

**Stage 3** 2d6 poison damage and –20-foot status penalty to all Speeds (1 round)

**Source:** `= this.source` (`= this.source-type`)
