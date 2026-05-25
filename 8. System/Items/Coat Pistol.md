---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Concealable]]", "[[Concussive]]", "[[Fatal d8]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small pistol is easily concealed inside a jacket or some other article of clothing. Rarely kept as a primary weapon, coat pistols are equally favored by clever assassins and traveling Alkenstar aristocrats.

**Source:** `= this.source` (`= this.source-type`)
