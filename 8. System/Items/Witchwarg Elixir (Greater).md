---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 1400}"
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

This elixir warms your core and improves your circulation. For 24 hours, you are protected from the effects of severe cold. You're also protected from extreme and incredible cold.

**Source:** `= this.source` (`= this.source-type`)
