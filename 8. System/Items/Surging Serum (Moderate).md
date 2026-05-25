---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Healing]]"]
price: "{'gp': 75}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Involuntary jolts and surges of energy move through the drinker's body as it restores normal muscle control. When you drink this elixir, it attempts to counteract each effect that's inflicting the [[Clumsy]] or [[Enfeebled]] condition on you, using a 4th-rank counteract and a +14 counteract modifier.

**Source:** `= this.source` (`= this.source-type`)
