---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Concealable]]", "[[Finesse]]", "[[Injection]]", "[[Parry]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This umbrella's ferrule is a hollow-tipped blade three to four inches in length and often overlooked as decorative. A receptacle inside the umbrella's shaft can be loaded with a single dose of injury poison and injected into a damaged target with the pull of a sliding trigger. Reinforced ribs enable you to parry and deflect blows with the umbrella's tear-resistant canopy.

**Source:** `= this.source` (`= this.source-type`)
