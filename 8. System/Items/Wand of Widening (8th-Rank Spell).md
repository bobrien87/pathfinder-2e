---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]", "[[Wand]]"]
price: "{'gp': 24000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The end of this wand is forked with a peridot setting.

**Activate** Cast a Spell; The activation takes `pf2:2` if the spell normally takes `pf2:1` to cast, or `pf2:3` if the spell normally take `pf2:2`

**Frequency** Once per day, plus overcharge

**Effect** You Cast the Spell, and increase its area. Add 5 feet to the radius of a burst that normally has a radius of at least 10 feet; add 5 feet to the length of a cone or line that is normally 15 feet long or smaller; or add 10 feet to the length of a larger cone or line.

**Craft Requirements** Supply a casting of a spell of the appropriate rank. The spell must have a casting time of `pf2:1` or `pf2:2`, can't have a duration, and must have an area of burst (10 feet or more), cone, or line.

**Source:** `= this.source` (`= this.source-type`)
