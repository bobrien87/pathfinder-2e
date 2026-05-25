---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 155}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Wolfsbane appears in folklore for its link to werecreatures. If you are afflicted with lycanthropy and survive Stage 3 of wolfsbane, you're immediately cured of the lycanthropy.

**Activate** A (manipulate)

**Saving Throw** DC 30 [[Fortitude]] save

**Onset** 10 minutes

**Maximum Duration** 6 minutes

**Stage 1** 3d10 poison damage (1 minute)

**Stage 2** 4d10 poison damage (1 minute)

**Stage 3** 5d10 poison damage (1 minute)

**Source:** `= this.source` (`= this.source-type`)
