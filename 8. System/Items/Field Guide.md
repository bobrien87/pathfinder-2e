---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This book contains illustrations and information on edible and dangerous plants. Most field guides tend to be region specific, such as the Mindspin Mountains or Osirian desert. If you are attempting to [[Subsist]] in the field guide's region with a skill you're untrained in, consulting the book gives you a +2 circumstance bonus to the skill check.

**Source:** `= this.source` (`= this.source-type`)
