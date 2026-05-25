---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Expandable]]"]
price: "{'gp': 175}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

The body of a fearsome tyrannosaurus is shrunken and contained in this bottle, its desiccated form barely constrained within the glass. The effigy of a Gargantuan tyrannosaurus forms when you open the bottle, causing devastation as it rampages. The tyrannosaurus Strides up to 40 feet. It can move through the spaces of Huge or smaller creatures and can attempt to Trample each creature whose space it enters, dealing @Damage[(2d10+12)[bludgeoning]] with a DC 27 [[Reflex]] save. It can attempt to Trample each creature only once.

**Craft Requirements** Supply the corpse of a tyrannosaurus.

**Source:** `= this.source` (`= this.source-type`)
