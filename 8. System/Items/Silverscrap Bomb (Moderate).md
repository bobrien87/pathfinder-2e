---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Splash]]"]
price: "{'gp': 255}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

Silverscrap bombs are compact clusters of silver shards that explode upon impact, shredding everything in the vicinity. The bomb grants a +2 item bonus to attack rolls and deals 3d4 piercing damage and 3 piercing splash damage. All damage from the bomb is treated as silver for the purposes of weaknesses, resistances, and the like.

**Source:** `= this.source` (`= this.source-type`)
