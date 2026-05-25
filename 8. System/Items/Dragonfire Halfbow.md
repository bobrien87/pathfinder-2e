---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Deadly d10]]", "[[Fire]]", "[[Magical]]", "[[Propulsive]]"]
price: "{'gp': 1800}"
usage: "held-in-one-plus-hands"
bulk: "1"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Crafted by layering bamboo with strips of sliced scales harvested from a fire-breathing dragon, this bow has a significant draw strength. This design is commonly seen in Hongal, as the shorter limb allows for easier maneuvering on horseback. While the wielder of this *+2 striking composite shortbow* is mounted, they apply the bow's item bonus to Nature checks to Command their mount.

**Activate—Dragon's Arrow** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You draw the bow back to its maximum draw length without nocking an arrow, and as you release the string, the dragonfire halfbow casts [[Fireball]] (heightened to 5th rank; DC 29 [[Reflex]] save), targeted at a point of your choosing within the spell's range. You and your mount are immune to the effects of this *fireball*.

**Source:** `= this.source` (`= this.source-type`)
