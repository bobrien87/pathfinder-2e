---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Fire]]", "[[Magical]]"]
price: "{'gp': 6500}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A weapon with this rune is empowered by flickering flame. The weapon deals an additional 1d6 fire damage on a successful Strike, plus 2d10 persistent fire damage on a critical hit.

Fire damage dealt by this weapon (including the persistent fire damage) ignores the target's fire resistance.

**Source:** `= this.source` (`= this.source-type`)
