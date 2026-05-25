---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Deadly d8]]", "[[Forceful]]", "[[Magical]]", "[[Reach]]", "[[Relic]]", "[[Wood]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 vitalizing striking glaive* is said to have been carved from a single branch of an ancient white ash tree deep in the Arthfell Forest. The grain of the weapon's blade is especially tight, giving the weapon both incredible durability and a finish that resembles silver and steel folded by a master smith.

**Source:** `= this.source` (`= this.source-type`)
