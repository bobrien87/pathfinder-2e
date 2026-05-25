---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 2000}"
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

After you drink this elixir, you notice subtle visual details. For the next hour, you gain a +3 item bonus to Perception checks, or +4 when attempting to find secret doors and traps.

Each time you pass within 10 feet of a secret door or trap, the GM automatically rolls a secret check for you to find it.

> [!danger] Effect: Eagle Eye Elixir

**Source:** `= this.source` (`= this.source-type`)
