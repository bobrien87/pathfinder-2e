---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Healing]]"]
price: "{'gp': 3}"
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

Elixirs of life accelerate a living creature's natural healing processes and immune system. Upon drinking this elixir, you regain 1d6 healing Hit Points and gain +1 item bonus to saving throws against diseases and poisons for 10 minutes.

> [!danger] Effect: Elixir of Life

**Source:** `= this.source` (`= this.source-type`)
