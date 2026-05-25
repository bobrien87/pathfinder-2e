---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Precious]]"]
price: "{'gp': 1000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The most rare and valuable skymetal, orichalcum is coveted for its incredible time-related magical properties. This dull, coppery metal isn't as physically sturdy as adamantine, but orichalcum's time-bending properties protect it, granting it greater Hardness and Hit Points. If an orichalcum item takes damage but isn't destroyed, it repairs itself completely 24 hours later.

Orichalcum ItemsOrichalcum ItemsHardnessHPBTThin ItemsHigh-grade166432ItemsHigh-grade187236StructureHigh-grade3514070

**Source:** `= this.source` (`= this.source-type`)
