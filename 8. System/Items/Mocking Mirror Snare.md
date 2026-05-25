---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Illusion]]", "[[Magical]]", "[[Mental]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A reflective rune is hidden in the snare's square. A creature that enters this square suddenly sees a twisted reflection of themself appear nearby and perform some action that they would never do. The creature takes 8d6 mental damage with a DC 25 [[Will]] save. On a critical failure, the creature is also [[Confused]] until the end of their next turn.

**Source:** `= this.source` (`= this.source-type`)
