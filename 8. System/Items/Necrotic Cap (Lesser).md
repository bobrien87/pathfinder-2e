---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 18}"
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

You can use this slimy, rotting mushroom as a spell catalyst when you cast an [[Acid Grip]] spell by tapping it against the target, causing the mushroom to release a cloud of necrotic spores. When you do, *acid grip* loses the acid trait, gains the fungus trait, and all acid damage the spell deals becomes void damage. On a hit, the target additionally gains the [[Enfeebled]] 1 and [[Sickened]] 1 conditions as the spores consume their flesh. As long as the target is taking persistent void damage, they can't reduce the value of their sickened condition below 1.

> [!danger] Effect: Necrotic Cap

**Source:** `= this.source` (`= this.source-type`)
