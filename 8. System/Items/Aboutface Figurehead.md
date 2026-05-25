---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Figurehead]]", "[[Magical]]", "[[Water]]"]
price: "{'gp': 980}"
usage: "attached-to-ships-bow"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** attached to a ship's bow

This otherwise plain-looking figurehead has the concerned expression of someone afraid they're being chased. If the vessel the figurehead is attached to has the sluggish vehicle ability, the figurehead suppresses that ability. Captains frequently give the ability to activate an *aboutface figurehead* to the person at the helm of their ship.

**Activate—About Face!** `pf2:1` (concentrate, move)

**Frequency** once per day

**Effect** The figurehead turns its head as if to look behind it, spawning a momentary whirlpool under the ship and turbulent winds directly opposite the ship's heading. The ship makes a 180-degree turn in place, then continues heading in this new direction starting next turn.

**Source:** `= this.source` (`= this.source-type`)
