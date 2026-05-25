---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Consumable]]", "[[Fire]]", "[[Magical]]"]
price: "{'gp': 520}"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** A (manipulate)

This piece of ammunition is coated in gritty black soot. When activated *greater explosive ammunition* hits a target, the missile explodes in a @Template[burst|distance:10], dealing @Damage[10d6[fire]|options:area-damage] damage to each creature in the area (including the target). Each creature must attempt a DC 30 [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
