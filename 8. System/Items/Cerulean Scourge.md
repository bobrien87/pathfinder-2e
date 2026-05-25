---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 1450}"
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

This poison is infamous for making the victim's blood vessels glow with a bright blue light before painfully bursting.

**Saving Throw** DC 37 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 10d6 poison damage (1 round)

**Stage 2** 12d6 poison damage (1 round)

**Stage 3** 14d6 poison damage (1 round)

**Source:** `= this.source` (`= this.source-type`)
