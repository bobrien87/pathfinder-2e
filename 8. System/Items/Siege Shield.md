---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]"]
price: "{'gp': 60}"
bulk: "4"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This massive tower shield (Hardness 5, HP 20, BT 10) is crafted from the toughest steel. It's not ideal for single combat, but it can be used to defend soldiers during a siege. While this shield is raised, you gain resistance to damage from siege weapons equal to half this shield's Hardness.

**Activate—Plant Cover** `pf2:1` (manipulate) You unequip the shield and prop it on the ground. The shield grants standard cover for one Medium or smaller creature in its square and lesser cover for a Large one.

**Source:** `= this.source` (`= this.source-type`)
