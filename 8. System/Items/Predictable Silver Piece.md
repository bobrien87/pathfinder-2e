---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Magical]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This seemingly unremarkable, weathered silver coin bears the bust of an unnamed monarch on the face and a majestic bird on the tail. You can toss the coin without activating it, in which case it follows the normal laws of probability.

**Activate—Cheat Fate** `pf2:1` (manipulate)

**Effect** You rub your thumb on one side of the coin with the intent of slightly tweaking the strands of fate, then flip the coin into the air in a coin toss. No matter how the toss is resolved- letting the coin fall to the ground, slapping it down on the back of your hand, or catching it on your open palm-it always lands with the side you rubbed face up.

**Source:** `= this.source` (`= this.source-type`)
