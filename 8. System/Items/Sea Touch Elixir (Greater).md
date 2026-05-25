---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Polymorph]]"]
price: "{'gp': 920}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

This briny concoction alters the skin on your hands and feet. The spaces between your fingers and toes become webbed, granting you a swim Speed of 20 feet for 24 hours, and you can breathe underwater.

> [!danger] Effect: Sea Touch Elixir (Greater)

**Source:** `= this.source` (`= this.source-type`)
