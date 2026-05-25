---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]", "[[Void]]"]
price: "{'gp': 160}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

Distilled from the Netherworld, this oily substance imposes tenebrous effects. The enfeebled condition from nethershade lasts for 24 hours.

**Saving Throw** DC 29 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 2d6 void damage and 2d6 poison damage (1 round)

**Stage 2** 3d6 void damage, 2d6 poison damage, and [[Enfeebled]] 1 (1 round)

**Stage 3** 3d6 void damage, 3d6 poison damage, and [[Enfeebled]] 2 (1 round)

**Source:** `= this.source` (`= this.source-type`)
