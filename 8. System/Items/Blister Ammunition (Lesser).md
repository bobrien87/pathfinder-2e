---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Poison]]"]
price: "{'gp': 21}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (manipulate)

Blister ammunition is loaded with alchemically processed irritants, such as pollen, pepper, and formic acid. A creature hit by activated blister ammunition must attempt a DC 19 [[Fortitude]] save or begin to itch uncontrollably for 3 rounds in addition to damage the attack normally deals. On a critical hit, increase the Fortitude DC by 2 (DC 21 [[Fortitude]] save), and the target is [[Dazzled]] for 1 round. For the duration, each time the target attempts a concentrate action, it must attempt a DC 8 flat check, losing the action on a failure. An affected creature can use a single Interact action to scratch and sneeze, allowing it to automatically pass the flat check. The effect ends early once an affected creature spends 3 Interact actions scratching and sneezing. These Interact actions don't need to be consecutive.

**Source:** `= this.source` (`= this.source-type`)
