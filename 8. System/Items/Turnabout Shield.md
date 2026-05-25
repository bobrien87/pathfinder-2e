---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Deflecting physical ranged]]", "[[Magical]]"]
price: "{'gp': 600}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The face of this standard-grade silver salvo shield (Hardness 7, HP 28, BT 14) is polished to a mirror finish.

**Activate** R (concentrate)

**Frequency** once per 10 minutes

**Trigger** A ranged Strike using ammunition such as arrows, bolts, or bullets (but not siege rounds or larger projectiles) misses you

**Requirements** You have the turnabout shield raised

**Effect** The ammunition enters the shield and is redirected with the same force with which it was originally fired. Make a ranged Strike using the ammunition with an attack modifier of +19, targeting a creature within 60 feet.

**Source:** `= this.source` (`= this.source-type`)
