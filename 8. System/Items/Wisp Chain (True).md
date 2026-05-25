---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Air]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 35000}"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+3 greater resilient chain shirt* is made of small, interlocking currents of wind carefully woven together. While the links of air don't jingle against each other like chain links might, the tiny cyclones nevertheless create a blustering howl akin to standing at the center of a storm. A creature that ends its turn adjacent to you must attempt a DC 39 [[Fortitude]] save. On a failure, it becomes [[Deafened]] until it moves away from you.

**Activate—Slicing Links** `pf2:2` (concentrate)

**Frequency** Once per day

**Effect** You unbind the currents that form your armor and release them as cutting whorls of air that slice into creatures in a @Template[cone|distance:60]. Creatures in the area take @Damage[16d6[slashing]|options:area-damage] damage with a DC 41 [[Fortitude]] save. A creature that fails its save is also pushed 10 feet (or 20 feet on a critical failure). You lose the AC bonus of your armor until the end of your turn, when the air currents reform the wisp chain around you.

**Source:** `= this.source` (`= this.source-type`)
