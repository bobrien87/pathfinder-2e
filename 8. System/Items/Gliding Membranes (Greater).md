---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 340}"
usage: "implanted"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Membranes that stretch between your arms and torso help you convert a fall into a glide. Treat falls as 50 feet shorter. Even if you take fall damage, you can land on your feet by succeeding at a DC 15 [[Acrobatics]] check.

**Source:** `= this.source` (`= this.source-type`)
