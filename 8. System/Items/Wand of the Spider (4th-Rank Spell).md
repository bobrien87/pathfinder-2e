---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]", "[[Poison]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 1400, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The length of this wand is a pair of twisted giant spider legs.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Web]] at 4th-rank, but the strands of webbing are toxic. Any creature that fails its Athletics check or Reflex save to navigate the web takes @Damage[2d6[poison],1d6[persistent,poison]]{2d6 poison damage plus 1d6 persistent poison damage}.

**Craft Requirements** Supply a casting of *web* at 4th-rank.

**Source:** `= this.source` (`= this.source-type`)
