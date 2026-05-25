---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 4}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You critically succeed at an attack roll with the affixed weapon.

The fulu explodes and showers the area with bright sparks. The struck creature takes an additional 1d4 sonic damage and must succeed at a DC 15 [[Fortitude]] save or be [[Dazzled]] for 1 round (or dazzled for 1 minute on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
