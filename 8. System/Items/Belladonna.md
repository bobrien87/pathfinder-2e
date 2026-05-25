---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Sometimes called "deadly nightshade," belladonna is a widely available toxin produced from a plant similar to a tomato.

**Saving Throw** DC 19 [[Fortitude]] save

**Onset** 10 minutes

**Maximum Duration** 30 minutes

**Stage 1** [[Dazzled]] (10 minutes)

**Stage 2** 1d6 poison damage and [[Sickened]] 1 (10 minutes)

**Stage 3** 1d6 poison damage, [[Confused]], and sickened 1 (1 minute)

**Source:** `= this.source` (`= this.source-type`)
