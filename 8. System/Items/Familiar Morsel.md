---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 30}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

*Familiar morsels* are little treats that come in a wide variety of flavors that appeal to numerous creatures. Each morsel is keyed to one familiar ability at its creation. When you feed the morsel to your familiar, it gains that familiar ability for 1 hour. If your familiar doesn't meet the requirements, or if it already has an ability from a *familiar morsel*, the morsel is nothing more than a pleasing snack, its magic wasted.

**Source:** `= this.source` (`= this.source-type`)
