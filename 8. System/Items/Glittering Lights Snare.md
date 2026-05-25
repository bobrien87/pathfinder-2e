---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Light]]", "[[Magical]]", "[[Snare]]", "[[Trap]]", "[[Visual]]"]
price: "{'gp': 25}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Some of Brastlewark's youth craft lesser versions of this snare to prank their friends. A creature that enters the square's square is subjected to a rapid series of flashing lights that overstimulate the senses. They must attempt a DC 22 [[Reflex]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Dazzled]] for 2 rounds.
- **Failure** The creature is dazzled for 1 minute.
- **Critical Failure** The creature is [[Blinded]] for 1 round and then dazzled for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
