---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 7}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

When you apply this thick, viscous oil to a weapon or suit of armor, that item immediately becomes magically potent. If the item is a weapon, it temporarily becomes a *+1 striking weapon*, or, if it's armor, it temporarily becomes *+1 resilient armor*. This lasts for 1 minute.

> [!danger] Effect: Oil of Potency

**Source:** `= this.source` (`= this.source-type`)
