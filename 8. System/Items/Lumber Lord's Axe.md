---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]", "[[Sweep]]"]
price: "{'gp': 900}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This unassuming tool wouldn't look out of place on the belt of an industrious laborer. Grooves worn into the wooden handle over years of use and an irregularly sharpened blade give it the distinct impression of being cherished, and the potent scent of freshly chopped wood always clings to the axe's blade despite any attempt to clean it or remove the odor. A creature that holds or carries this *+2 striking cold iron battle axe* feels an obligation to tell the truth and receives a –4 status penalty to its attempts to Lie. A lumber lord's axe deals 1d6 additional slashing damage to creatures with the fungus or plant trait, as long as the creatures aren't disguised as non-fungus or non-plant creatures. It's up to GM discretion whether this additional damage applies against a creature disguised as a fungus or plant creature.

**Activate—Transformative Polish** 1 minute (manipulate)

**Frequency** once per day

**Effect** You polish and sharpen the axe, after which its scent grows even more powerful and the axe's blade transforms into your choice of standard-grade adamantine or standard-grade dawnsilver for 1 hour; then after this duration, the woodcutter's axe reverts to cold iron.

> [!danger] Effect: Lumber Lord's Axe

**Source:** `= this.source` (`= this.source-type`)
