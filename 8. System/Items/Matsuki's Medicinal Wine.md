---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 12}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Old Matsuki's private brew has quite the kick. In addition to making you tipsy, this medicinal wine works wonders in helping to recover from disease. When you drink a dose of this wine you must succeed at a DC 18 [[Fortitude]] save to avoid becoming [[Off Guard]] for 10 minutes (and also [[Clumsy]] 1 for this duration if you critically fail the saving throw). Regardless of the saving throw's results, you gain a +2 item bonus to Fortitude saving throws against diseases and poisons for the next 24 hours. This applies to your daily save against a disease's progression as well.

> [!danger] Effect: Matsuki's Medicinal Wine

**Source:** `= this.source` (`= this.source-type`)
