---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Light]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 20, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This luminescent white gem glows from within, and a weapon it's applied to gains its inner radiance, shedding dim light in a 10-foot radius. Successful Strikes with a weapon affected by a *limning gem* outline the target in a bright white light; if the target was [[Invisible]], it becomes [[Concealed]] instead. This light lasts until the end of your next turn or for the remainder of the *limning gem*'s duration on a critical hit.

**Source:** `= this.source` (`= this.source-type`)
