---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 330}"
usage: "worn"
bulk: "L"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The intricate beading of this shawl subtly guides you. While you wear the shawl, you always know which direction is north and gain a +1 item bonus to Survival checks.

**Activate—Mind's Map** `pf2:1` (concentrate)

You focus your mind's eye on a location you've been to previously. The beads on the shawl shift colors to create a map of the area based on your memories. You can dismiss this effect as a free action.

**Source:** `= this.source` (`= this.source-type`)
