---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]", "[[Virulent]]", "[[Void]]"]
price: "{'gp': 525}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder #203: Shepherd of Decay"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

Derived from duskwood sap tapped during the winter solstice, this toxin erodes the connection between body and soul, tricking the latter into assuming the former has already died. Survivors of this near-death experience report ominous tunnel vision, as if the Grim Reaper lurks in their peripheral vision and awaits their final breath.

**Saving Throw** DC 30 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 2d12 void damage and [[Doomed]] 1 for 1 round (1 round)

**Stage 2** 3d12 void damage and doomed 1 for 1 round (1 round)

**Stage 3** 3d12 void damage and doomed 1 (1 round)

**Stage 4** 3d12 void damage and [[Doomed]] 2 (1 round)

**Source:** `= this.source` (`= this.source-type`)
