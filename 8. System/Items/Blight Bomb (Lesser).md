---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Poison]]", "[[Splash]]"]
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

Blight bombs contain volatile toxic chemicals that rot flesh. A blight bomb deals 1d4 poison damage, 1d4 persistent poison damage, and 1 poison splash damage.

**Source:** `= this.source` (`= this.source-type`)
