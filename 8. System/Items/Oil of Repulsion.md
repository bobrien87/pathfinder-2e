---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 175}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

This oil contains magnetically charged iron filings repelled into opposite ends of the vial. For 1 minute after you apply this oil to armor, any creature that hits you with a melee Strike must attempt a DC 28 [[Fortitude]] save with the following effects.
- **Success** The creature is unaffected.
- **Failure** The creature is pushed up to 10 feet away from you (the GM determines the direction).
- **Critical Failure** As failure, and the creature is also knocked [[Prone]].

**Source:** `= this.source` (`= this.source-type`)
