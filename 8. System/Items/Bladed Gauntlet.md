---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Finesse]]", "[[Free hand]]", "[[Modular]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A dagger attached to a retractable mechanism is integrated in this gauntlet's dorsum, so a combatant can quickly arm themself with a blade to exploit the weak points in an enemy's armor. Switching configurations on the gauntlet reveals or retracts the contained dagger as appropriate. The dagger isn't removable, and thus can't be wielded or etched with runes separately from the gauntlet.

**Source:** `= this.source` (`= this.source-type`)
