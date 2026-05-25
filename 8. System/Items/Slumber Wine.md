---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]", "[[Sleep]]"]
price: "{'gp': 325}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Slumber wine sees its greatest use in games of intrigue, where an absence can be more devastating than injury. Characters unconscious from slumber wine can't wake up by any means while the poison lasts, don't need to eat or drink while unconscious in this way, and appear to be recently dead unless an examiner succeeds at a DC 40 [[Medicine]] check.

**Activate** A (manipulate)

**Saving Throw** DC 32 [[Fortitude]] save

**Onset** 1 hour

**Maximum Duration** 7 days

**Stage 1** [[Unconscious]] (1 day)

**Stage 2** [[Unconscious]] (2 days)

**Stage 3** [[Unconscious]] (3 days)

**Source:** `= this.source` (`= this.source-type`)
