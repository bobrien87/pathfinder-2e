---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Fire]]", "[[Splash]]"]
price: "{'gp': 2500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A Strike

Alchemist's fire is a combination of volatile liquids that ignite when exposed to air. Alchemist's fire deals 4d8 fire damage, 4 persistent fire damage, and 4 fire splash damage. You gain a +3 item bonus to attack rolls.

**Source:** `= this.source` (`= this.source-type`)
