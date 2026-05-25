---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Magical]]", "[[Plant]]", "[[Wood]]"]
price: "{'gp': 6500}"
usage: "etched-onto-melee-weapon"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Small roots grow along the surface of the weapon, clinging tightly to its contours. On a critical hit with the weapon, roots grow from the target. It's [[Immobilized]] for 1 round (`act escape show-dc=all dc=34`) and [[Clumsy]] 1 for as long as the immobilization lasts.

**Source:** `= this.source` (`= this.source-type`)
