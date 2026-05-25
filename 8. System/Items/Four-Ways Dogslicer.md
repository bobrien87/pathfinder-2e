---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Agile]]", "[[Backstabber]]", "[[Cold]]", "[[Electricity]]", "[[Finesse]]", "[[Fire]]", "[[Goblin]]", "[[Magical]]"]
price: "{'gp': 1700}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 striking dogslicer* is obviously the work of a brilliant but scrappy artisan who valued versatility over safety. Four toothy gems line the blade's cutting edge, three of which glow-one with fiery red light, one with a chill blue, and one that gives off sparks-while the last is a glistening black. Each of these gems embodies a weapon property rune, but only one rune can be active at a time.

**Activate-Gem Twist** `pf2:1` (manipulate)

**Effect** You twist the gem along the blade corresponding with the desired weapon rune: red for *flaming*, blue for *frost*, or yellow for *shock*. You take 1d6 untyped damage of the type the chosen rune deals. You can instead twist the black gem to disable the active property rune, taking no damage.

**Source:** `= this.source` (`= this.source-type`)
