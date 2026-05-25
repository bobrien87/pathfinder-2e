---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]", "[[Reach]]"]
price: "{'gp': 465}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking longspear* of polished white bone features a tip of layered reptilian scales, compressed to form a sharp edge. Akki crafted this spear herself after she and her allies tangled with a hydra plaguing the marshes outside Aelyosos. She pressed the scales of the creature down into a spearpoint mostly through sheer stubbornness, granting it a unique ability.

**Activate—Hydra Swipe** `pf2:2`

**Frequency** once per hour

**Effect** The spearhead unravels and elongates into a group of snake heads. Make up to three melee Strikes with the *Hydra Spear*, each at a different creature within 20 feet. These attacks do not count toward your multiple attack penalty until all attacks have been resolved.

**Source:** `= this.source` (`= this.source-type`)
