---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 15}"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (manipulate)

Etched with the symbol of a ram's head, activated battering ammunition magically gathers momentum as it flies, imparting this momentum to its target on a successful Strike. It deals bludgeoning damage instead of its normal damage type and pushes the target 5 feet on a successful hit.

**Source:** `= this.source` (`= this.source-type`)
