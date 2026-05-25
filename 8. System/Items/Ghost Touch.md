---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]"]
price: "{'gp': 75}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A weapon etched with this rune can harm creatures without physical form. A *ghost touch* weapon is particularly effective against incorporeal creatures, which almost always have a specific vulnerability to *ghost touch* weapons.

Incorporeal creatures can touch, hold, and wield *ghost touch* weapons (unlike most physical objects).

**Source:** `= this.source` (`= this.source-type`)
