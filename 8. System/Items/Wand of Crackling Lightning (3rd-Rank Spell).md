---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Electricity]]", "[[Magical]]", "[[Wand]]"]
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

This wand is made of two copper plates and a ceramic center.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Lightning Bolt]] at 3rd-rank, but the spell's area is twice as wide (two adjacent and parallel @Template[line|distance:120|width:10]{120-foot lines}) and creatures that fail their save are [[Off Guard]] for 1 round.

**Craft Requirements** Supply a casting of *lightning bolt* at 3rd-rank.

**Source:** `= this.source` (`= this.source-type`)
