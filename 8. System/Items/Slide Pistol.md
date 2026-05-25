---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Capacity 5]]", "[[Concussive]]", "[[Fatal d10]]"]
price: "{'gp': 16}"
usage: "held-in-one-hand"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Also known as a harmonica gun, this weapon is essentially a stock, trigger, and firing mechanism attached to a sliding brace of barrels that can each hold a round of ammunition.

**Source:** `= this.source` (`= this.source-type`)
