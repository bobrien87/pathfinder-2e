---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 22}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

**Requirements** You are trained in Thievery

This small silver skeleton key can be pinned to armor or a sleeve. When you turn the key to activate it, you gain a +1 status bonus to Thievery checks to [[Pick a Lock]] for 1 minute. The first time you get a success or critical success on an attempt to Pick a Lock, you achieve one additional success toward opening a complex lock.

> [!danger] Effect: Sneaky Key

**Source:** `= this.source` (`= this.source-type`)
