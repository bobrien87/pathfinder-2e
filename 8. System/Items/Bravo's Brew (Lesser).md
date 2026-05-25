---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mental]]"]
price: "{'gp': 7}"
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

This flask of foaming beer grants courage. For the next hour after drinking this elixir, you gain a +1 item bonus to Will saves, or +2 when attempting Will saves against fear.

> [!danger] Effect: Bravo's Brew

**Source:** `= this.source` (`= this.source-type`)
