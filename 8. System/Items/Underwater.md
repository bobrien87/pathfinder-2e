---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]", "[[Water]]"]
price: "{'gp': 50}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This weapon works as well in water as it does on land. Attacks with the weapon don't take the normal penalties and restrictions for being used in water or underwater. If the weapon is capable of dealing fire damage, its fire functions underwater as well.

**Source:** `= this.source` (`= this.source-type`)
