---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Occult]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This oversized greataxe, infamous for the chilling laughter it emits whenever it takes a life, was crafted by the frost giant sorcerer Jorngarl from the final blade named Toothy Morris after it was stolen in an attack on a Gray Gardener convoy. It functions as a *+3 major striking vorpal greataxe* that retains the unique properties of a [[Final Blade]], trapping the souls of any it slays and preventing them from being returned to life by any means short of divine intervention, even a [[Wish]] ritual or similar magic.

**Source:** `= this.source` (`= this.source-type`)
