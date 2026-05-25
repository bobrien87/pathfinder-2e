---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A pair of conjoined sahkils known as The Dancers created this poison for the Ninth Army. While stupefied by this poison, a creature can't treat any creature as its ally.

**Saving Throw** DC 23 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 6 days

**Stage 1** 2d8 poison damage and [[Stupefied 1]] (1 day)

**Stage 2** 3d8 poison damage and [[Stupefied 2]] (2 days)

**Stage 3** 4d8 poison damage and [[Stupefied 4]] (3 days)

**Source:** `= this.source` (`= this.source-type`)
