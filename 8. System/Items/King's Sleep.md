---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]", "[[Virulent]]"]
price: "{'gp': 4000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

King's sleep is an insidious long-term poison that can seem like a disease or even death from natural causes on a venerable target. The drained condition from king's sleep is cumulative with each failed save and can't be removed while the poison lasts.

**Saving Throw** DC 41 [[Fortitude]] save

**Onset** 1 day

**Stage 1** [[Drained]] 1 (1 day)

**Stage 2** [[Drained]] 1 (1 day)

**Stage 3** [[Drained]] 2 (1 day)

**Source:** `= this.source` (`= this.source-type`)
