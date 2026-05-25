---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Contact]]", "[[Poison]]"]
price: "{'gp': 110}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A paste made by mashing the fine, threadlike roots of a certain creeper vine, spider root renders a victim clumsy and maladroit.

**Activate** A (manipulate)

**Saving Throw** DC 28 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 6 minutes

**Stage 1** 3d6 poison damage and [[Clumsy]] 1 (1 minute)

**Stage 2** 4d6 poison damage and [[Clumsy]] 2 (1 minute)

**Stage 3** 6d6 poison damage and [[Clumsy]] 3 (1 minute)

**Source:** `= this.source` (`= this.source-type`)
