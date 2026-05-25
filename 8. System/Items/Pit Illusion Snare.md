---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Illusion]]", "[[Magical]]", "[[Mental]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 9}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You add a touch of illusion magic to a magical sensor that makes the target believe a bottomless pit opens below it when the snare is triggered. A Medium or smaller creature that enters the snare's square must attempt a DC 20 [[Will]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is cautious moving forward, treating the snare's square and all adjacent squares as difficult terrain until the end of its turn.
- **Failure** The creature falls [[Prone]].
- **Critical Failure** The creature falls prone and takes 1d4 mental damage.

**Source:** `= this.source` (`= this.source-type`)
