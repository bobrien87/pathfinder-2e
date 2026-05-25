---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Splash]]"]
price: "{'gp': 360}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

This bomb is made of volatile fluids that rapidly expand and harden when exposed to air. A boulder seed grants a +2 item bonus to attack rolls and deals 3d4 bludgeoning damage and 3 bludgeoning splash damage, according to the bomb's type. When activated, the bomb fills a 5-foot cube with hardened foam, it creates a boulder as hard as wood (Hardness 5, HP 20) that pushes Medium or smaller targets. On a critical hit, the target also falls [[Prone]]. The splash zone fills with rubble, creating difficult terrain. The "boulder" the bomb creates fails all saving throws and loses 1 Hardness per round, disintegrating into fine powder when the boulder's Hardness is reduced to 0. At that time, the difficult terrain the bomb created also disappears.

**Source:** `= this.source` (`= this.source-type`)
