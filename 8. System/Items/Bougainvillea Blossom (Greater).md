---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 300}"
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

This pink flower has long, slender thorns along the stem. The flower can be used as a catalyst when casting an [[Entangling Flora]] spell, which causes the affected plants to sprout long thorns and vibrant pink blossoms. The area becomes hazardous terrain, dealing 3 piercing damage to an enemy each time it enters an affected square.

**Source:** `= this.source` (`= this.source-type`)
