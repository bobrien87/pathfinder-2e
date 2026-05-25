---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Capacity 4]]", "[[Free hand]]", "[[Parry]]"]
price: "{'gp': 9}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The gauntlet bow is a heavy metal glove with a built-in crossbow and rotating chamber mechanism for easy reloading. A gauntlet bow can be used to make melee attacks like a standard gauntlet, and it retains any valid runes when used as such. You can't reload a gauntlet bow with the hand wielding it.

**Source:** `= this.source` (`= this.source-type`)
