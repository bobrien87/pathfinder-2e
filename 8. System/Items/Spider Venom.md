---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 25}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This venom erodes its target's defenses, aiding the spider in securing prey.

**Activate** `pf2:2` (manipulate)

**Saving Throw** DC 22 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 1d10 poison damage and [[Sickened]] 1 (1 round)

**Stage 2** 1d12 poison damage, [[Clumsy]] 1, and [[Sickened]] 2 (1 round)

**Stage 3** 2d6 poison damage, [[Clumsy]] 2, and [[Sickened]] 3 (1 round)

**Source:** `= this.source` (`= this.source-type`)
