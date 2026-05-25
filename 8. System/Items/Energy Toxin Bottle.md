---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Cursed]]", "[[Magical]]", "[[Potion]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This glass bottle embellished with brass decorations appears to be a lesser energy breath potion of a specific type, but has been polluted, making it toxic to use.

**Activate** `pf2:1` (manipulate)

**Effect** You drink from the bottle and must succeed at a DC 25 [[Fortitude]] save saving throw or become [[Sickened]] 1 ([[Sickened]] 2 on a critical failure) and immediately vomit the potion directly onto yourself, taking 5d6 untyped damage of the same damage type the potion deals and expending the item. If you succeed at your Fortitude save, you become sickened 1 but otherwise are able to unleash Energy Breath as normal for a *lesser energy breath potion* of the appropriate type.

**Source:** `= this.source` (`= this.source-type`)
