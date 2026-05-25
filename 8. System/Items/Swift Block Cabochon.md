---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 70}"
usage: "affixed-to-a-shield"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** R (concentrate)

**Trigger** You would take damage from a physical attack while you are wielding the affixed shield

This clear quartz cabochon attaches to the center of your shield. When you activate the cabochon, use the [[Shield Block]] reaction even if you don't have the shield raised and even if you don't normally have that reaction. Increase the shield's Hardness by 5 against the triggering attack. The shield remains raised after the block.

> [!danger] Effect: Swift Block Cabochon

**Source:** `= this.source` (`= this.source-type`)
