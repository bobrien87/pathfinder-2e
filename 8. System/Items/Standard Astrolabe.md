---
type: item
source-type: "Remaster"
level: "2"
price: "{'gp': 30}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate—Calculate** 1 minute (manipulate)

Astrolabes can be used for navigation in unfamiliar or featureless locations. To use an astrolabe, the holder must be trained in Survival. By spending 1 minute to measure the height of the stars and planets, a holder who knows the time and date can determine the latitude, and a holder who knows their latitude can determine the date and time. An astrolabe also grants a +1 item bonus to checks to identify celestial bodies. A standard astrolabe functions only on steady ground.

**Source:** `= this.source` (`= this.source-type`)
