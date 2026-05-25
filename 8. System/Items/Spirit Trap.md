---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Magical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A spirit trap consists of a net dipped in water that has been steeped with sacred herbs to better combat phantoms. This snare's components function as a net when not set up. You set this snare up in a 10-foot-by-10-foot area. The first creature with the spirit trait that steps into the area must attempt a DC 16 [[Fortitude]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Off Guard]] for 1 round.
- **Failure** The creature is [[Immobilized]] for 1 round.
- **Critical Failure** The creature is immobilized until it Escapes (DC 16).

**Source:** `= this.source` (`= this.source-type`)
