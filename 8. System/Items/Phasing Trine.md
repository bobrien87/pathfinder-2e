---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 1900, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A *phasing trine* is a metallic triangle embedded with a clear crystal designed in the shape of a bow and nocked arrow. Strikes made with a ranged weapon under the effect of a *phasing trine* against a target who is observed by or [[Hidden]] to you (but not [[Undetected]]) pass through any non-magical barriers or walls in their way, though magical barriers stop the ammunition. These Strikes ignore all cover and circumstance bonuses to AC from shields.

> [!danger] Effect: Phasing Trine

The Strike's damage can't be reduced with a [[Shield Block]] reaction using a non-magical shield.

**Source:** `= this.source` (`= this.source-type`)
