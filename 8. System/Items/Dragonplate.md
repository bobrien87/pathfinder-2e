---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Bulwark]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 10000}"
bulk: "4"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This suit of +2 *greater resilient dragonhide full plate* makes you look like a fearsome dragon. The armor comes in many different varieties depending on the type of dragon from which it's made, though they usually conform to the four magical traditions.

**Activate—Dragon Breath** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You unleash a @Template[cone|distance:15] of energy with a damage type and saving throw corresponding to the tradition of the dragon used to make the armor (shown on the table below). The cone deals 14d6 damage; each creature in the area must attempt a DC 36 basic saving throw.

**Craft Requirements** The initial raw materials must include 1,250 gp of dragonhide.

Dragon TraditionDamageArcane@Damage[14d6[force]|options:area-damage]{Force} (DC 36 [[Reflex]] save{Reflex})Divine@Damage[14d6[spirit]|options:area-damage]{Spirit} (DC 36 [[Reflex]] save{Reflex})Occult@Damage[14d6[mental]|options:area-damage]{Mental} (DC 36 [[Will]] save{Will})Primal@Damage[14d6[poison]|options:area-damage]{Poison} (DC 36 [[Fortitude]] save{Fortitude})

**Source:** `= this.source` (`= this.source-type`)
