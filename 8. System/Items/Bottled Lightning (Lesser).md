---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Electricity]]", "[[Splash]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A Strike

Bottled lightning is packed with volatile reagents that create a blast of electricity when they are exposed to air. Bottled lightning deals 1d6 electricity damage and 1 electricity splash damage. On a hit, the target becomes [[Off Guard]] until the start of your next turn.

**Source:** `= this.source` (`= this.source-type`)
