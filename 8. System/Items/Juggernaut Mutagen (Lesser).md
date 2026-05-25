---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

Your body becomes sturdy and ponderous.

**Benefit** You gain a +1 item bonus to Fortitude saves and 5 temporary Hit Points. Whenever you are at maximum Hit Points for at least 1 full minute, you regain the temporary Hit Points.

**Drawback** You take a -2 penalty to Will saves, Perception checks and initiative rolls.

**Duration** 1 minute.

> [!danger] Effect: Juggernaut Mutagen (Lesser)

**Source:** `= this.source` (`= this.source-type`)
