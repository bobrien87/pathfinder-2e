---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Deadly d6]]", "[[Finesse]]", "[[Thrown 20]]", "[[Versatile s]]"]
price: "{'gp': 2}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

From a central metal ring, four tapering metal blades extend like points on a compass rose. When gripping a starknife from the center, the wielder can use it as a melee weapon. It can also be thrown short distances.

**Source:** `= this.source` (`= this.source-type`)
