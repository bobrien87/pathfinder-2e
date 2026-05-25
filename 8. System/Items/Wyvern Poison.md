---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 80}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Properly harvested and preserved, the poison from a wyvern's sting is effective and direct.

**Activate** `pf2:2` (manipulate)

**Saving Throw** DC 26 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 3d6 poison damage (1 round)

**Stage 2** 3d8 poison damage (1 round)

**Stage 3** 3d10 poison damage (1 round)

**Source:** `= this.source` (`= this.source-type`)
