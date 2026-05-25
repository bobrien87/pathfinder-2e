---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Mythic]]", "[[Poison]]"]
price: "{'gp': 100}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Mythotoxin is exceedingly difficult to produce, as it requires fresh venom from a mythic creature that must then be distilled into a more concentrated form. Mythic creatures take a –2 circumstance penalty to saves against mythotoxin.

**Saving Throw** DC 26 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 3d6 poison damage (1 round)

**Stage 2** 3d8 poison damage (1 round)

**Stage 3** 3d10 untyped damage and lose 1 Mythic Point, or become [[Doomed]] 1 if you have no Mythic Points to lose (1 round; doomed condition value has normal duration)

**Source:** `= this.source` (`= this.source-type`)
