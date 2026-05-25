---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]", "[[Misfortune]]"]
price: "{'gp': 22}"
usage: "affixed-to-a-ranged-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Duration** 1 hour

Incorporating green in its writing, a *discord fulu* is a popular but unethical tool often deployed on romantic rivals to foil their advances. While the fulu is affixed to it, a creature treats its attitude toward other creatures as one step worse than it is. The creature also takes a –1 status penalty to Diplomacy checks. The first failure the creature rolls on a Diplomacy check becomes a critical failure instead, and the fulu turns to ash, ending its effect.

> [!danger] Effect: Discord Fulu

**Source:** `= this.source` (`= this.source-type`)
