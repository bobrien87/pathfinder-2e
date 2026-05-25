---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Magical]]", "[[Wood]]"]
price: "{'gp': 20}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A fine case carved from elegant wood, this tinderbox holds twigs and strips of wood in a selection of six colors. In a typical *versatile tinderbox*, these colors are black, blue, green, magenta, yellow, and violet. When used in lighting a fire, colored tinder alters the flames' color and smoke to match. The box is perfectly carved and constructed to hold tinder, keeping it completely dry, but is incapable of closing if used to hold anything else. The tinderbox replenishes itself; it's never out of tinder when its owner is in need, but it never produces a surplus of tinder either.

**Source:** `= this.source` (`= this.source-type`)
