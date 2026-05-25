---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 50}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate)

This cube of blackened iron is affixed to a weapon with an iron chain. When you activate the cube, make a melee Strike. If it hits and deals damage, you can attempt an Athletics check to [[Trip]] the creature you hit. If this knocks the target [[Prone]], the target takes 2d6 bludgeoning damage from the force of the impact. If you're wielding a two-handed melee weapon, you can ignore Trip's requirement that you have a free hand. Both attacks count toward your multiple attack penalty, but the penalty doesn't increase until after you've made both of them.

If you have the [[Slam Down]] feat, ignore the normal size restrictions for the trip and increase the damage dice if you knock the target prone to the damage die of your weapon if it's higher than d6.

**Source:** `= this.source` (`= this.source-type`)
