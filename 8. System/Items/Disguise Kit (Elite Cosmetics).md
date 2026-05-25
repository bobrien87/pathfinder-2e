---
type: item
source-type: "Remaster"
level: "3"
price: "{'sp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small wooden box contains cosmetics, false facial hair, spirit gum, and a few simple wigs. You usually need a disguise kit to set up a disguise in order to Impersonate someone using the Deception skill. An elite disguise kit adds a +1 item bonus to relevant checks. If you've crafted a large number of disguises, you can replenish your cosmetics supply with replacement cosmetics suitable for the type of your disguise kit.

**Source:** `= this.source` (`= this.source-type`)
