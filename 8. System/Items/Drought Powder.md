---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Earth]]", "[[Magical]]"]
price: "{'gp': 250}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A gray powder that smells like wet rock, *drought powder* has various uses against water. If you sprinkle it over your body, you and items you carry or wear remain dry for the next 24 hours. Thrown into a body of water, the dust lowers the water in an area 50 feet long by 50 feet wide by 10 feet. You can fling it in the air, coating all creatures in a @Template[burst|distance:10] centered on a point within 5 feet of you. Creatures who have the water trait in that area are affected as if by a [[Slow]] spell (DC 28). If you attempt to use the dust in other, similar ways, the GM decides whether the dust can accomplish your aims.

**Source:** `= this.source` (`= this.source-type`)
