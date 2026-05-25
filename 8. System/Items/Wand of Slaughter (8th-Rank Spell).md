---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]", "[[Void]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 24000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This polished black wand has a green gem at the tip, and anyone who looks into it sees a reflection of a grinning skull.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Execute]] at 8th-rank. If the spell slays a living target, the corpse releases grim energy in a @Template[emanation|distance:20], dealing 16 void damage.

**Craft Requirements** Supply a casting of *execute* at 8th-rank.

**Source:** `= this.source` (`= this.source-type`)
