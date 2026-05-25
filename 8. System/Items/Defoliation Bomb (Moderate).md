---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Splash]]", "[[Void]]"]
price: "{'gp': 18}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

This brightly painted ceramic sphere contains chemicals that cause plants to wither and die. You gain a +1 item bonus to attack rolls. A defoliation bomb deals the 2d6 void damage, 2d4 persistent void damage, and 2 void splash damage to all plants in the area. Non-creature plants in the area immediately wither and die.

**Source:** `= this.source` (`= this.source-type`)
