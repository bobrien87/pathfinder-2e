---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Contact]]", "[[Poison]]"]
price: "{'gp': 55}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Tangle root toxin sees use to impede opponents in athletic competitions, in addition to espionage and tracking.

**Saving Throw** DC 26 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 6 minutes

**Stage 1** [[Clumsy]] 1 and –10-foot status penalty to all Speeds (1 minute)

**Stage 2** [[Clumsy]] 2 and –20-foot status penalty to all Speeds (1 minute)

**Stage 3** [[Clumsy]] 3, [[Off Guard]], and –30-foot status penalty to all Speeds

**Source:** `= this.source` (`= this.source-type`)
