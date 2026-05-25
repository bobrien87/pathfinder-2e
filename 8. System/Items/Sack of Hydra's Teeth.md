---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 1800, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This soft cotton bag has a drawstring of sinew and a jagged embroidery pattern around the mouth. Inside are a seemingly endless number of needle-sharp teeth.

**Activate—Sow a Tooth** `pf2:2` (manipulate, occult)

**Frequency** once per hour

**Effect** You cast forth a tooth from the bag, and where it lands, a skeleton springs up from the ground. This has the effect of [[Phantasmal Minion]], except the minion appears as a visible skeleton.

**Activate—Fist Full of Fangs** `pf2:2` (manipulate, occult)

**Frequency** once per day

**Effect** You draw a whole handful of teeth and cast them to the ground, casting [[Rouse Skeletons]] as a 5th-rank spell (DC 30).

**Source:** `= this.source` (`= this.source-type`)
