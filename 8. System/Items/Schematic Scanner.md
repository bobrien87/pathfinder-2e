---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]"]
price: "{'gp': 230}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #215: To Blot Out the Sun"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *schematic scanner* is a complex brass device featuring multiple mounted lenses, clamps, and apertures. A *schematic scanner* can hold the formulas for items as if it were a formula book with unlimited capacity. You can add a formula to the *schematic scanner* using the Store Schematics activation. A *schematic scanner* grants you a +2 item bonus to Crafting checks to craft an item whose formula is stored in the *schematic scanner*.

**Activate—Store Schematics** `pf2:3` (manipulate)

You place the written formula for an item into the *schematic scanner* and view it through the mounted lenses, magically storing a copy of the formula inside the *schematic scanner*.

**Activate—Reverse Engineer Schematics** (manipulate)

You place an item in front of the *schematic scanner*, then view the item through the mounted lenses, magically learning the formula for the targeted item, without disassembling or causing harm to the item, and storing the formula in the *schematic scanner*. Reverse engineering a formula in this way takes 10 minutes and doesn't cost any gold.

**Source:** `= this.source` (`= this.source-type`)
