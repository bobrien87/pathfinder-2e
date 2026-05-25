---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Fire]]", "[[Magical]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 1000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The luminous design of red-orange cracks on this black obsidian wand suggests cooling lava.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast 4th-rank [[Floating Flame]]. If you create the flame on the ground, the ground in the sphere's square and all adjacent squares are coated in rolling flames until the start of your next turn. These are difficult terrain and hazardous terrain. A creature that moves on the ground takes 3 fire damage for every square of rolling flames it moves into. If a creature in the flames doesn't move on its turn, it takes the damage for each of the squares it's in at the end of its turn. The first time you Sustain the Spell each round, the sphere creates rolling flames again in its new location (or the same location if you chose not to move it), provided it's on the ground.

**Craft Requirements** Supply a casting of *floating flame* of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
