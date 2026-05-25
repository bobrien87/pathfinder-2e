---
type: item
source-type: "Remaster"
level: "21"
traits: ["[[Apex]]", "[[Artifact]]", "[[Divine]]", "[[Intelligent]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "worncape"
bulk: "L"
source: "Pathfinder #206: Bring the House Down"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This black cape flows more like a vaporous liquid than fabric. The cape grants you a +3 item bonus to Stealth checks. When you invest the cape, you either increase your Dexterity score by 2 or increase it to 18, whichever is higher.

**Activate** R Interact

**Frequency** once per hour

**Trigger** A creature misses you with an attack

**Effect** Attempt a Stealth check against the triggering creature's Perception DC. If you roll a success, you're [[Hidden]] from that creature until the end of your next turn or until right after you use a hostile action against that creature. If you roll a critical success, you're hidden from that creature until the end of your next turn, even if you use hostile actions against that creature.

**Activate** `pf2:2` Interact

**Frequency** once per day

**Effect** With a twirl of the cape, you transform yourself into a puff of gray smoke. You cast [[Vapor Form]] on yourself.

**Source:** `= this.source` (`= this.source-type`)
