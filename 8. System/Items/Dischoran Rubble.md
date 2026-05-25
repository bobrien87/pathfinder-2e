---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 18}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell (add 1 action)

Rock fragments exposed to any dischoran's sonic blasts can sometimes retain a portion of the attack's energy, trembling slightly whenever they are touched. When you cast [[Noise Blast]] using a piece of *dischoran rubble*, the cacophony reverberates through the targets' forms for 1 round. If a creature that failed or critically failed its initial saving throw moves 10 feet or more on their next turn, it takes an additional 2d10 sonic damage.

**Source:** `= this.source` (`= this.source-type`)
