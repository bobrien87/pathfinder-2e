---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Concussive]]", "[[Scatter 10]]"]
price: "{'gp': 6}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This weapon fires pellets from a trumpet-shaped barrel, making it an excellent choice for hunting brush fowl or dealing damage within a short, broad area. Adventuring gunslingers often carry a blunderbuss to deal with swarms of vermin and similar threats.

**Source:** `= this.source` (`= this.source-type`)
