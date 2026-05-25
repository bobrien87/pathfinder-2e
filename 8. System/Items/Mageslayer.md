---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Forceful]]", "[[Magical]]", "[[Sweep]]"]
price: "{'gp': 500}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This roughly forged *+1 striking scimitar* is a favorite instrument of battlefield operatives seeking to weaken an enemy's forces by strategically eliminating their magical support. A mageslayer deals an additional 1d6 spirit damage to any creature it Strikes that's capable of casting spells from the arcane tradition. When wearing or wielding a mageslayer, you gain resistance 5 to damage from spells from the arcane tradition.

**Source:** `= this.source` (`= this.source-type`)
