---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 500}"
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

Venom from enormous cave worms leaves a victim weakened.

**Saving Throw** DC 32 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 5d6 poison damage and [[Enfeebled]] 2 (1 round)

**Stage 2** 6d6 poison damage and enfeebled 2 (1 round)

**Stage 3** 8d6 poison damage and enfeebled 2 (1 round)

**Source:** `= this.source` (`= this.source-type`)
