---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Cold]]", "[[Magical]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 4500, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wand is a slender length of ice-blue glass.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Howling Blizzard]] at 5th-rank. Snow lingers in the spell's area, remaining as difficult terrain for 1 minute.

**Craft Requirements** Supply a casting of *howling blizzard* at 5th-rank.

**Source:** `= this.source` (`= this.source-type`)
