---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Consumable]]"]
price: "{'gp': 5}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Monster Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Many calignis keep several doses of darkening poison, an uncommon injury poison made from Darklands spider venom, on hand to incapacitate foes.

**Saving Throw** DC 16 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 1d6 poison (1 round)

**Stage 2** 1d6 poison and creatures you can see only with darkvision are [[Concealed]] from you (1 round)

**Stage 3** 1d6 poison and creatures you can see only with darkvision are [[Hidden]] from you (1 round).

**Source:** `= this.source` (`= this.source-type`)
