---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]"]
price: "{'gp': 340}"
usage: "etched-onto-piercing-or-slashing-melee-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Weapons with *wounding* runes are said to thirst for blood. When you hit a creature with a *wounding* weapon, you deal an extra 1d6 persistent bleed damage.

**Source:** `= this.source` (`= this.source-type`)
