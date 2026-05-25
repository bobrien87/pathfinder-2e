---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 2}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While gunslingers have many methods for practicing their aim, these sturdy paper targets are excellent for tracking a gunslinger's progress over time, keeping score of how close they came to hitting the most vital spots. These targets are also used in situations where more detailed accuracy must be recorded, such as firearm competitions. Practice targets can appear in many shapes and sizes and usually come in packs of 10 held in protective cases made of heavy cloth or light leather.

**Source:** `= this.source` (`= this.source-type`)
