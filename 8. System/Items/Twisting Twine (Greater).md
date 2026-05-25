---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]"]
price: "{'gp': 300}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ball of hempen twine resists efforts to unravel it by hand.

**Activate—Unravel Twine** `pf2:1` (manipulate)

**Effect** You toss the ball of twine into a square within 20 feet. The twine then unravels and animates, attempting to [[Disarm]] or [[Trip]] (your choice) a creature in the square with a total of +15 to the Athletics check. At the end of your turn, the twine winds itself back into a ball and returns to your hand; if you don't have a free hand, it returns to your space instead.

**Source:** `= this.source` (`= this.source-type`)
