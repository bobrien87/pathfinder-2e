---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Agile]]", "[[Concealable]]", "[[Finesse]]", "[[Illusion]]", "[[Magical]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This elegant *+1 striking sword cane* serves equally well as a fashionable accessory and hidden weapon suitable for high-society events where weapons aren't typically permitted.

**Activate-Hide Magic** A (manipulate)

**Effect** You twist the sword cane's hilt, magically merging the blade into the cane. While the blade is merged, it can't be drawn and gains the benefits of a 3rd-rank [[Disguise Magic]] spell to appear non-magical. Passive observers can't attempt a check to notice the cane is anything more than a mundane, if superb, fashion accessory. Those carefully examining it can discern the cane is more than it appears, but doing so is extremely difficult (DC 30 [[Perception]] check). Activating the sword cane again releases the blade, allowing it to be drawn normally.

**Source:** `= this.source` (`= this.source-type`)
