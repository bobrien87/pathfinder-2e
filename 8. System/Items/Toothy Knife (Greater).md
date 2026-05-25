---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'gp': 1100}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This jagged bit of metal is pitted and worn but wickedly sharp. The DC of the flat check to end persistent bleed damage dealt by a weapon under the effects of a *greater toothy knife* is 19 (or 14 with appropriate assistance). This bleeding still typically ends on its own after 1 minute, as normal.

> [!danger] Effect: Toothy Knife

**Source:** `= this.source` (`= this.source-type`)
