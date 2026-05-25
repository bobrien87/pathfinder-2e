---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These brass goggles are engraved with flame patterns and have thick, heavy lenses.

While worn, they give you a +3 item bonus to Crafting checks to [[Craft]] alchemical items. When making Strikes with alchemical bombs, you ignore lesser cover.

If your Strike with an alchemical bomb fails (but doesn't critically fail), you gain a +3 item bonus to the splash damage the target of the Strike takes.

**Source:** `= this.source` (`= this.source-type`)
