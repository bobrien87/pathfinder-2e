---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]", "[[Virulent]]"]
price: "{'gp': 8500}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder #206: Bring the House Down"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Vyre's Bliss is a toxin that looks and tastes like fine wine.

**Saving Throw** DC 43 [[Fortitude]] save

**Maximum Duration** 24 hours

**Stage 1** [[Off Guard]] and [[Stupefied 1]] (1 round)

**Stage 2** off-guard, [[Clumsy]] 1, and [[Stupefied 2]] (1 round)

**Stage 3** off-guard, [[Clumsy]] 2, and [[Stupefied 3]] (1 round)

**Stage 4** clumsy 2, stupefied 3, and [[Unconscious]] (8 hours)

**Source:** `= this.source` (`= this.source-type`)
