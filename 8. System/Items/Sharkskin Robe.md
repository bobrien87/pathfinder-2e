---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Invested]]", "[[Magical]]", "[[Water]]"]
price: "{'gp': 1900}"
usage: "wornclothing"
bulk: "1"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This sandy-textured robe comes with sleeves that resemble dorsal fins. It's believed to have been developed by frustrated alchemists from the Universe for trips to the Plane of Water. The *sharkskin robe* grants you a swim Speed equal to your land Speed and a +2 item bonus to Athletics checks.

**Activate—Shark's Elegance** `pf2:2` (concentrate, manipulate)

**Frequency** once per hour

**Effect** For 1 minute, any time you make a Strike, your weapon or unarmed attack gains the benefit of the *underwater* weapon property rune.

> [!danger] Effect: Sharkskin Robe

**Source:** `= this.source` (`= this.source-type`)
