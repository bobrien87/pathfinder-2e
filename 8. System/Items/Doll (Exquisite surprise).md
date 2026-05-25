---
type: item
source-type: "Remaster"
level: "2"
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder NPC Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This doll contains a hidden compartment or pouch capable of holding a single object of up to light Bulk—typically a bell, rattle, or dried flowers.

Hiding an object inside this beautifully crafted surprise doll grants you a +1 item bonus to Stealth checks made to Conceal an Item, as the compartment is particularly well-hidden and weighted to ensure the doll doesn't feel off-balance with an item inside.

**Source:** `= this.source` (`= this.source-type`)
