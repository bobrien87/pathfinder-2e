---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]"]
price: "{'gp': 1300}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The strings of this spider-shaped lute are made from the webbing of a goliath spider and the tuning pegs are crafted from the spider's spinnerets. An *arachnolute* grants you a +2 item bonus to Performance checks while playing music with the instrument.

**Activate—Web Chord** `pf2:2` (manipulate)

**Frequency** once per hour

**Effect** Sticky webbing sprays in a @Template[cone|distance:30] as you strum the lute's strings. Each creature in the area of the webbing is [[Immobilized]] unless it succeeds at a DC 29 [[Reflex]] save.

**Craft Requirements** The initial materials must include the spinnerets of a goliath spider, as well as a spool of its webbing.

**Source:** `= this.source` (`= this.source-type`)
