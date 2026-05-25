---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Inhaled]]", "[[Poison]]"]
price: "{'gp': 6}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

Brave alchemists take great care to capture a tatzlwyrm's poisonous vapor in small vials, typically through a system of compressors that can concentrate their exhalations.

**Saving Throw** DC 15 [[Fortitude]] save

**Maximum Duration** 3 rounds

**Stage 1** [[Sickened]] 1 (1 round)

**Stage 2** 2d6 poison damage and [[Enfeebled]] 1 (1 round)

**Stage 3** 4d6 poison damage and enfeebled 1 (1 round)

**Source:** `= this.source` (`= this.source-type`)
