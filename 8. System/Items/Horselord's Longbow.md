---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Deadly d10]]", "[[Magical]]", "[[Volley 30]]"]
price: "{'gp': 250}"
usage: "held-in-one-plus-hands"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These *+1 striking longbows*, usually decorated with intricate animal carvings and hawk feathers, are a favored weapon among the mounted warriors of the Shriikirri-Quah clan in north-central Varisia, although Shoanti travel widely enough that they find frequent use by cavalries of other nations and cultures as well. While you are mounted, Strikes with this bow gain a +2 circumstance bonus to damage against unmounted creatures who are smaller than your mount.

**Source:** `= this.source` (`= this.source-type`)
