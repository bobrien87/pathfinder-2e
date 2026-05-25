---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 55}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell (add 1 action)

This palm-sized chunk of wood it rotting, and riddled with mold and fungi. You can crush this wood to use it as a spell catalyst when you cast a [[Oaken Resilience]]. When you do, the bark that covers your skin is rotting, and emits a small cloud of spores whenever your hurt. For the duration, whenever you take physical damage, your rotting bark skin emits a cloud of spores in a @Template[emanation|distance:5]. Creatures in the area must attempt a DC 21 [[Fortitude]] save to avoid taking @Damage[1d4[poison]|options:area-damage] damage.

**Source:** `= this.source` (`= this.source-type`)
