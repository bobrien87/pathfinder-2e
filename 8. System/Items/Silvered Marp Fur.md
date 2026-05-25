---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 110}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

A marp that gnaws on silver rather than gold grows fur tipped with silver that can be further processed into a versatile spell catalyst. A spellcaster who uses *silvered marp fur* with an [[Impaling Spike]] spell creates a silver spike rather than a cold iron one.

**Source:** `= this.source` (`= this.source-type`)
