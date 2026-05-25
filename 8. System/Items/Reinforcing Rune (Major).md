---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Magical]]"]
price: "{'gp': 8000}"
usage: "etched-onto-a-shield"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Reinforcing runes make a shield significantly more durable, allowing it to effectively block more powerful attacks.

The shield's Hardness increases by 5, it gains an additional 84 Hit Points, and its BT increases by 42 (maximum 17 Hardness, 136 HP, and 68 BT).

**Source:** `= this.source` (`= this.source-type`)
