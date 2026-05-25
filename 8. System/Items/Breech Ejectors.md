---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]"]
price: "{'gp': 10}"
usage: "attached-to-firearm"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These spring-loaded inserts can be fitted into the breech of a double-barreled firearm over the course of 10 minutes or during the firearm's daily maintenance. After the weapon is fired, the ejectors hasten the reloading process by ejecting the spent detritus from the fired rounds. This allows you to reload both barrels of the double-barreled weapon as a single Interact action the next time you reload the weapon as long as you do so before the end of your next turn. However, the ejectors are consumed in the process, and you must spend the time to insert a new set to gain the benefit again.

**Source:** `= this.source` (`= this.source-type`)
