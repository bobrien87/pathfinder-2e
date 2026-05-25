---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Artifact]]", "[[Divine]]", "[[Invested]]"]
price: "{'value': {}}"
usage: "worngarment"
bulk: "—"
source: "Pathfinder Monster Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Each *flawless celestial shawl* functions only for a specifc tennin and is the culmination of their immortal cultivation. The sash is made of celestial silken threads stronger than adamantine yet lighter than gossamer. The tennin can draw thread from the *flawless celestial shawl* to serve as a sterling artisan's toolkit and workshop to [[Craft]]. The sash can be used to work with precious materials of any grade. On any Crafting check the tennin attempts using the shawl, they use the outcome one degree of success better than the result of their roll.

**Activation—Reweave** `pf2:3`

The tennin uses the sash to [[Repair]] an item. This Repair activity loses the exploration trait.

**Source:** `= this.source` (`= this.source-type`)
