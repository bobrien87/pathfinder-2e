---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 50, 'pp': 0, 'sp': 0}"
usage: "worngarment"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Only a fool would march an army into a freezing climate without adequate protection. This thick parka with a hood protects you from even the harshest of conditions. You negate the damage from severe environmental cold, reduce the damage from extreme cold to that of severe cold, and reduce the damage from incredible cold to extreme cold.

**Activate—Extra Warming** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You draw the hood of your warming parka closed to fend off the cold as much as possible. For the next minute, you gain resistance 3 to cold damage, but also take a –2 item penalty to Perception checks. You can Dismiss this effect.

> [!danger] Effect: Extra Warming

**Source:** `= this.source` (`= this.source-type`)
