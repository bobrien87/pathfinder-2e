---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Aura]]", "[[Magical]]"]
price: "{'gp': 100}"
usage: "affixed-or-held-in-one-hand"
bulk: "—"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This peach-colored magical banner offers the promise of a good watch and a comfortable sleep. You and allies within the banner's aura gain a +1 item bonus to Perception DCs and protection from severe cold and heat.

**Source:** `= this.source` (`= this.source-type`)
