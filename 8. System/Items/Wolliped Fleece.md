---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell (add one action)

A small bundle of *wolliped fleece* contains the memory of winter snows. Adding this catalyst to a casting of [[Chilling Spray]] coats all squares within the area of effect with a thin layer of ice. These squares become difficult terrain until the beginning of your next turn.

**Source:** `= this.source` (`= this.source-type`)
