---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Darkness]]", "[[Magical]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 1000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wand is a length of wrought black iron.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Darkness]] at 4th-rank. Each creature that ends its turn within the spell's area must succeed at a DC 27 [[Will]] save or become [[Frightened]] 1 ([[Frightened]] 2 on a critical failure).

**Craft Requirements** Supply a casting of *darkness* at 4th-rank.

**Source:** `= this.source` (`= this.source-type`)
