---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 40}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Scorpion venom is excruciating and its effects are somewhat debilitating.

**Activate** `pf2:2` (manipulate)

**Saving Throw** DC 22 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 2d6 poison damage and [[Enfeebled]] 1 (1 round)

**Stage 2** 2d8 poison damage and [[Enfeebled]] 1 (1 round)

**Stage 3** 2d10 poison damage and [[Enfeebled]] 2 (1 round)

**Source:** `= this.source` (`= this.source-type`)
