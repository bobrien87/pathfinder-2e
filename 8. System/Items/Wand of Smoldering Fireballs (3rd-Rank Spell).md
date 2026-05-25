---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Fire]]", "[[Magical]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 500, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This blackened, heavily burned stick smells faintly of saltpeter.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Fireball]] at 3rd-rank. Each creature that fails its save takes 1d6 persistent,fire damage.

**Craft Requirements** Supply a casting of *fireball* at 3rd-rank.

**Source:** `= this.source` (`= this.source-type`)
