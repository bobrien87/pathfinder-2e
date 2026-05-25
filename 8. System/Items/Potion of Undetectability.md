---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Consumable]]", "[[Illusion]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 4400}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

Drinking this dull-black liquid makes you undetectable to detection effects.

This grants the same effects as [[Hidden Mind]] but without the bonus against mental effects. You also gain the effects of a 4th-rank [[Invisibility]] spell, which protects against [[See the Unseen]] spells of 8th rank and lower and has a DC of 36 against [[Truesight]].

The potion's effects last for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
