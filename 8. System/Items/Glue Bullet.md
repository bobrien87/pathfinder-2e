---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 16}"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** round

**Activate** `pf2:1` (manipulate)

These cartridges are filled with sticky clear glue. When a glue bullet hits, a syrupy webbing coats the target and sticks to the ground or a nearby surface, hindering their movement. The target takes a –10-foot circumstance penalty to its Speeds for 2d4 rounds, or until it Escapes against a DC of 18. On a critical hit, the target is also [[Immobilized]] until it Escapes.

> [!danger] Effect: Glue Bullet

**Source:** `= this.source` (`= this.source-type`)
