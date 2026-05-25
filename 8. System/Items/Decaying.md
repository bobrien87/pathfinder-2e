---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]", "[[Void]]"]
price: "{'gp': 500}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Eerie waves of purplish energy dance across the surface of a weapon etched with this rune. When you hit with the weapon, add 1d4 void damage to the damage dealt. In addition, on a critical hit, the target takes 2d4 persistent void damage; if the target has a shield raised, the shield takes the same amount of persistent damage (its wielder rolls the flat check to see if the persistent damage ends, or the GM rolls if the shield is no longer in someone's possession). Unlike normal void damage, the void damage from a *decaying* rune damages objects, constructs, and the like by eroding them away.

**Source:** `= this.source` (`= this.source-type`)
