---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Morph]]"]
price: "{'gp': 13}"
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

Your fists become hard as stone. For 1 hour, your fists deal 1d6 bludgeoning damage and lose the nonlethal trait.

> [!danger] Effect: Stone Fist Elixir

**Source:** `= this.source` (`= this.source-type`)
