---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]"]
price: "{'gp': 500}"
usage: "affixed-to-load-bearing-wall-or-pillar"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Duration** 1 week

Despite the name, a kaiju fulu protects a building against damage of all sorts. When an affixed structure no larger than 100 feet × 100 feet and up to 50 feet tall takes damage, the structure is as hard as standard-grade adamantine against that damage and any damage that occurs within 1 hour thereafter. The fulu then crumbles to dust, and its effects end.

**Source:** `= this.source` (`= this.source-type`)
