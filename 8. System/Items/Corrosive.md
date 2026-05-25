---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Acid]]", "[[Magical]]"]
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

Acid sizzles across the surface of the weapon. When you hit with the weapon, add 1d6 acid damage to the damage dealt. In addition, on a critical hit, the target's armor (if any) takes 3d6 acid damage (before applying Hardness); if the target has a shield raised, the shield takes this damage instead.

**Source:** `= this.source` (`= this.source-type`)
