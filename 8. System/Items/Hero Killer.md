---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Mythic]]", "[[Poison]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Crafted from nightshade plants that grow near sites of mythic power, this poison wreaks havoc on those with a mythic calling.

**Saving Throw** DC 28 [[Fortitude]] save

**Onset** 1 round

**Maximum Duration** 5 rounds

**Stage 1** 3d6 poison damage and lose 1 Mythic Point (1 round)

**Stage 2** 4d6 poison and [[Stupefied 1]] (1 round)

**Stage 3** 6d6 poison damage, [[Stupefied 2]], and lose all Mythic Points (1 round)

**Source:** `= this.source` (`= this.source-type`)
