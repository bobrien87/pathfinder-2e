---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 2000}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 resilient studded leather armor* is a gruesome amalgamation of skulls and bones from various creatures held in place with straps of leather that resemble sinew. When you wear this armor, you reek of death, and you can display these trappings in such a way that strikes fear in the hearts of your enemies.

**Activate—Unveil Fear** `pf2:r` (concentrate, occult)

**Frequency** once per hour

**Trigger** A creature moves within 30 feet of you

**Effect** You cast [[Fear]] on the target (DC 30 [[Will]] save).

**Craft Requirements** Supply a casting of fear.

**Source:** `= this.source` (`= this.source-type`)
