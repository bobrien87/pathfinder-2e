---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 950}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Long black feathers cover the leather pieces of this *+1 resilient leather armor*. The armor gives you the ability to glide safely to earth from high above the battlefield. It also grants you a +2 item bonus to Stealth checks you attempt while in the air.

**Activate—Soar** `pf2:1` (manipulate)

**Effect** You glide slowly toward the ground, 5 feet down and 30 feet forward through the air. Provided you spend at least 1 action gliding on your turn and haven't yet reached the ground, you remain in the air at the end of your turn. Otherwise, you fall.

**Source:** `= this.source` (`= this.source-type`)
