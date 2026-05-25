---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Concussive]]", "[[Fatal d10]]"]
price: "{'gp': 5}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The most commonly available of firearms in Alkenstar, the flintlock musket includes an external firing mechanism and an efficient and relatively compact frame. Though lacking the range and firing power of the arquebus preferred by Alkenstar and Dongun Hold's military members, the flintlock musket is popular among civilians for its ease of use.

**Source:** `= this.source` (`= this.source-type`)
