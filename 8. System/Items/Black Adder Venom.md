---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 6}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Adder venom is a simple but effective way to enhance a weapon.

**Activate** `pf2:2` (manipulate)

**Saving Throw** DC 18 [[Fortitude]] save

**Maximum Duration** 3 rounds

**Stage 1** 1d4 poison damage (1 round)

**Stage 2** 1d6 poison damage (1 round)

**Stage 3** 1d8 poison damage (1 round)

**Source:** `= this.source` (`= this.source-type`)
