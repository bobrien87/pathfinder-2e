---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Aura]]", "[[Consumable]]"]
price: "{'gp': 20}"
usage: "worngarment"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This magnetized suit is strapped to your body over your armor or clothes. When you Activate it, you must choose whether to set it to attract or repel. After being activated, the suit provides the listed benefits for the chosen activation type for 10 minutes before the magnets burn out and the suit becomes useless. While set to attract, you take a –1 status penalty to your AC against attacks made by metal weapons, while allies within a @Template[type:emanation|distance:10] gain a +1 status bonus to their AC. If set to repel, you gain a +1 status bonus to AC against attacks made with metal weapons.

While attracting metal, you gain a +1 status bonus to Athletics checks to Climb metal objects and [[Grapple]] metal creatures and a –1 status penalty to Athletics checks to [[Shove]] metal creatures. While repelling metal, you gain a +1 status bonus to Athletics checks to Shove metal creatures, but you take a –1 status penalty to Climb metal objects and Grapple metal creatures.

**Source:** `= this.source` (`= this.source-type`)
