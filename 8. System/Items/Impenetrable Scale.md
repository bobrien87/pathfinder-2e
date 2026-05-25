---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 12800}"
bulk: "3"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Made of overlapping, lustrous black scales of standard-grade adamantine, this +2 *greater resilient [[Fortification]] adamantine scale mail* seems to momentarily thicken at the point of impact when hit.

Whenever the armor's *fortification* rune successfully turns a significant foe's critical hit into a normal hit, one of the scales on the armor turns violet. You gain resistance to physical damage equal to the number of violet scales, to a maximum of 8.

At dawn each day, all the violet scales return to normal.

**Craft Requirements** The initial raw materials must include 1,600 gp of adamantine.

> [!danger] Effect: Impenetrable Scale

**Source:** `= this.source` (`= this.source-type`)
