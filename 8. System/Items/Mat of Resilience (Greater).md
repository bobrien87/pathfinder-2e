---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]"]
price: "{'gp': 1800}"
usage: "other"
bulk: "1"
source: "Pathfinder #209: Destroyer's Doom"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This light but sturdy woven mat, a miniature version of the floating foundations used in villages of the Dirt Sea, is carried tied in a tight roll. When you use an action to unfurl the mat onto an unoccupied horizontal space, the mat covers the existing terrain to create a smooth surface that can be walked on as if it were solid ground. Difficult or hazardous terrain in that square may be treated as normal while the mat of resilience covers it. The mat can be rolled back up or moved to an adjacent square using an Interact action, but it cannot be moved or put away while a creature is atop it.

**Activate—Steady Ground** `pf2:1` (envision)

You unfurl the mat and choose which shape it takes, either a @Template[square|distance:20] or a @Template[line|distance:40]{40-foot by 5-foot line}.

**Activate—Sturdy Foundation** `pf2:1` (manipulate)

**Requirements** A creature is atop the mat

**Effect** The creature enters a simple stance that makes the most of the mat's stabilizing magic. While in this stance, if at least half of the creature's space is atop the mat, it cannot gain the [[Off Guard]] condition.

**Source:** `= this.source` (`= this.source-type`)
