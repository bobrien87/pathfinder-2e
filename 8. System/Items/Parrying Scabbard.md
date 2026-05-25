---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You can draw this reinforced sheath during the same Interact action you use to draw the weapon it holds, wielding the weapon in one hand and the scabbard in your other. A parrying scabbard can be used for your defense much like a weapon with the parry trait: you can spend an action to position it defensively, gaining a +1 circumstance bonus to AC until the start of your next turn. Parrying scabbards are available for any sword that can be wielded in one hand.

> [!danger] Effect: Parry

**Source:** `= this.source` (`= this.source-type`)
