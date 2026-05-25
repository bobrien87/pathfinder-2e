---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Cold]]", "[[Consumable]]", "[[Splash]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

The bright blue liquid reagents in this vial rapidly absorb heat when exposed to air. A frost vial deals 3d6 cold damage and 3 cold splash damage. On a hit, the target takes a –10-foot status penalty to its Speeds until the end of its next turn. You gain a +2 item bonus to attack rolls.

> [!danger] Effect: Frost Vial

**Source:** `= this.source` (`= this.source-type`)
