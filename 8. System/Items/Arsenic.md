---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This toxin is a compound of arsenic and other substances. You can't reduce your sickened condition while affected.

**Activate** A (manipulate)

**Saving Throw** DC 18 [[Fortitude]] save

**Onset** 10 minutes

**Maximum Duration** 5 minutes

**Stage 1** 1d4 poison damage and [[Sickened]] 1 (1 minute)

**Stage 2** 1d6 poison damage and [[Sickened]] 2 (1 minute)

**Stage 3** 1d8 poison damage and [[Sickened]] 3 (1 minute)

**Source:** `= this.source` (`= this.source-type`)
