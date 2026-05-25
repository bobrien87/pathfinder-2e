---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Precious]]"]
price: "{'gp': 500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Dawnsilver is renowned for its lightness, durability, and effectiveness against a range of creatures including devils and werecreatures. It has the same sheen as silver but a slightly lighter hue. Dawnsilver weapons and armor are treated as if they were silver for the purpose of damaging creatures with weakness to silver. A metal item made of dawnsilver is lighter than one made of iron or steel: the item's Bulk is reduced by 1 (reduced to light Bulk if its normal Bulk is 1, with no effect on an item that normally has light Bulk). The Price of an item made of this material is based on the item's normal Bulk, not its reduced Bulk for being made of dawnsilver, but reduce the Bulk before making any further Bulk adjustments for the size of the item.

Dawnsilver ItemsDawnsilver ItemsHardnessHPBT**Thin Items**Standard-grade52010High-grade83216**Items**Standard-grade93618High-grade124824**Structure**Standard-grade187236High-grade249648

**Source:** `= this.source` (`= this.source-type`)
