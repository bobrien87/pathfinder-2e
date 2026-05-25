---
type: item
source-type: "Remaster"
level: "1"
price: "{'gp': 18}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A blade launcher has a bow-like assembly mounted on a handled frame. The frame can be configured to fire either a dagger, dart, shuriken, or starknife. Configuring a blade launcher requires three Interact actions. Once properly configured, loading an appropriate thrown weapon into a blade launcher requires a single Interact action. A blade launcher can't fire weapons for which it's not currently configured. A weapon fired with a blade launcher loses the agile, monk, thrown, and versatile traits, if it has them, and has a range increment of 40 feet. Due to losing the thrown weapon trait, returning and most other effects that allow a weapon to return don't function; even if a launched weapon did return, you'd still need to load it into the blade launcher with an Interact action to fire the blade launcher again.

**Source:** `= this.source` (`= this.source-type`)
