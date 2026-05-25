---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Magical]]", "[[Shove]]"]
price: "{'gp': 6250}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking maul* is a marvel of magical and mechanical engineering, designed thousands of years ago by the mages of the Jistka Imperium for the express purpose of disabling any of the Imperium's countless magical constructs and automatons that might turn against their creators. When you damage a construct with a Strike from the Jistkan colossus crusher, you deal an additional 1d6 persistent force damage. Additionally, whenever you critically hit a construct with this weapon, the Jistkan colossus crusher briefly disrupts the magical energy signature animating the construct; it must succeed a DC 35 [[Fortitude]] save or become [[Stunned]] 1.

**Source:** `= this.source` (`= this.source-type`)
