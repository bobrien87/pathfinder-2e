---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 670}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This elegant copper ring has miniature images of songbirds engraved around its circumference. You gain a +2 item bonus to Deception checks.

**Activate—Throw Voice** `pf2:2` (manipulate)

**Frequency** any number of times per day

**Effect** Twisting the ring around your finger allows you to magically throw your voice, with the effects of a 2nd-rank [[Ventriloquism]] spell (DC 27 [[Perception]] check).

**Source:** `= this.source` (`= this.source-type`)
