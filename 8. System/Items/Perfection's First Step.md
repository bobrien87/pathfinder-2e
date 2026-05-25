---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Mental]]", "[[Occult]]", "[[Water]]"]
price: "{'gp': 23}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (concentrate)

This palm-leaf manuscript contains an incomplete philosophical treatise about perfection, which you must complete and provide written commentaries upon before you can activate it. This activity takes 10 minutes, but can occur at any time before you activate the treatise.

When you activate *perfection's first step*, you cast [[Unbreaking Wave Advance]] with a save DC of 19. You are then temporarily immune to benefiting from further copies of *perfection's first step* until your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
