---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 15}"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (manipulate)

This ammunition includes a small reservoir of a tacky red substance that coats the ammunition when you activate it. The substance makes a creature bleed more freely. For 1 minute after you deal damage to a creature with an activated exsanguinating ammunition that creature gains weakness 1 to persistent bleed damage. In addition, the DC of any flat checks to end persistent bleed damage increases from 15 to 17 (from 10 to 12 when receiving particularly effective assistance) for the duration.

> [!danger] Effect: Exsanguinating Ammunition

**Source:** `= this.source` (`= this.source-type`)
