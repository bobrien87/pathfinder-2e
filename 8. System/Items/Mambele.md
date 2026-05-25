---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Deadly d8]]", "[[Disarm]]", "[[Thrown 20]]"]
price: "{'sp': 6}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Also known as a hunga munga or danisco, this knife-axe hybrid consists of a hilt and a blade that curves backward toward the wielder. The curve of the blade is such that after a victim has been struck by a mambele, more damage is dealt as the weapon is extracted from the victim's body.

**Source:** `= this.source` (`= this.source-type`)
