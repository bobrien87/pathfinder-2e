---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Agile]]", "[[Fire]]", "[[Free hand]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 20000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Prized by naari geniekin who prefer to fight with their fists, *true scalding gauntlets* are a pair of *+3 greater striking greater flaming spiked gauntlets*. The intricate golden gauntlets are engraved with Pyric writing praising the glories of the Dominion of Flame and embellished with shimmering black and red gemstones. A creature you grab or restrain while wearing the gauntlets must succeed at a DC 36 [[Fortitude]] save or take 4d6 persistent,fire damage and be [[Sickened]] 1 from the pain; it's temporarily immune to being sickened by *scalding gauntlets* for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
