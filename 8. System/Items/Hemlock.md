---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 2250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Concentrated hemlock is a particularly deadly toxin that halts muscle action-including that of the victim's heart.

**Activate** A (manipulate)

**Saving Throw** DC 38 [[Fortitude]] save

**Onset** 30 minutes

**Maximum Duration** 60 minutes

**Stage 1** 16d6 poison damage and [[Enfeebled]] 2 (10 minutes)

**Stage 2** 17d6 poison damage and [[Enfeebled]] 3 (10 minutes)

**Stage 3** 18d6 poison damage and [[Enfeebled]] 4 (10 minutes)

**Source:** `= this.source` (`= this.source-type`)
