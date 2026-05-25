---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Splash]]", "[[Void]]"]
price: "{'gp': 255}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

Atrophy bombs contain powerful chemicals developed by Urgathoan alchemists that sap a living creature's strength and drain their energy. The bomb deals 3d4 persistent void damage and 3 void splash damage, and the target is [[Enfeebled]] 2 until the start of your next turn. You gain a +2 item bonus to attack rolls with this bomb.

**Source:** `= this.source` (`= this.source-type`)
