---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 40}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This satchel includes 50 feet of rope, pulleys, a dozen pitons, a hammer, a grappling hook, and one set of crampons. Climbing kits allow you to attach yourself to the wall you're Climbing, moving half as quickly as usual (minimum 5 feet) but letting you attempt a DC 5 flat check whenever you critically fail to prevent a fall.

You gain a +1 item bonus to Athletics checks to Climb while using an extreme climbing kit. A single kit has only enough materials for one climber; each climber needs their own kit. If you wear your climbing kit, you can access it as part of a Climb action.

**Source:** `= this.source` (`= this.source-type`)
