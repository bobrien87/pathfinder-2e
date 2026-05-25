---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 110}"
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

Enzymatic compounds in this elixir strengthen and excite the muscles in your legs. You gain a +10 foot status bonus to your Speed for 1 hour.

> [!danger] Effect: Cheetah's Elixir (Greater)

**Source:** `= this.source` (`= this.source-type`)
