---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]"]
price: "{'gp': 19000}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *maestro's instrument* can be crafted in the form of any variety of handheld musical instruments. A *maestro's instrument* grants you a +3 item bonus to Performance checks while playing music with the instrument.

**Activate—Charming Performance** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You play the instrument, causing it to cast a 8th-rank [[Charm]] spell with DC 38.

**Craft Requirements** You must supply a casting of *charm* of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
