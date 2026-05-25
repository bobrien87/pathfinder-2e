---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Brace]]", "[[Deadly d12]]", "[[Magical]]", "[[Reach]]"]
price: "{'gp': 1900}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A sleek and impossibly lightweight blade attached to a haft scriven with lightning bolts make up this *+2 greater striking nodachi*.

**Activate—Prepare Flash** `pf2:2` (concentrate)

**Frequency** once per 10 minutes

**Effect** You concentrate with complete focus on your surroundings, breathing in the flashblade's magic to make you lighter and faster, and the blade of your sword more flexible. You Ready a melee Strike, increasing the flashblade's reach for that Strike to 20 feet. If the trigger doesn't occur, this doesn't count against the flashblade's frequency.

**Source:** `= this.source` (`= this.source-type`)
