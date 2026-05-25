---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Deadly d8]]", "[[Magical]]", "[[Two hand d10]]", "[[Versatile p]]"]
price: "{'gp': 700}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking ghost touch katana* is made from a whisker stolen from the king of cats over 300 years ago by a catfolk rogue named Vashu Vigaru. He sought the magic of the whisker to preternaturally extend his life, and some believe he still lives, having successfully divested himself of the sword to escape the king's wrath in the end.

**Activate—Whisker's Sense** `pf2:f` (concentrate)

**Frequency** once per hour

**Trigger** Your turn ends

**Effect** You extend your senses through the blade, allowing you to react to nearby movement. *Vashu's Ninth Life* gains the parry trait and raises itself into parrying position, granting you a +1 circumstance bonus to AC until the start of your next turn.

> [!danger] Effect: Vashu's Ninth Life

**Activate—Full of Life** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** You slay a living creature with *Vashu's Ninth Life*

**Effect** A portion of the slain creature's life force travels through the blade and into your soul, bolstering your own life. You gain the benefits of the Diehard feat for 1 minute. This causes you to die from the dying condition at dying 5 rather than dying 4.

**Source:** `= this.source` (`= this.source-type`)
