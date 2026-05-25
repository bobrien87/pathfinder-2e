---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Fire]]", "[[Magical]]"]
price: "{'gp': 1400}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Resembling *frozen lava*, an eternal eruption is made with the same type of time magic, but is built to loop through time, reforming itself after it's used. Determining the difference between the two requires a close examination to see a faint, repeating pattern of red runes.

**Activate—Lava Bomb** `pf2:2` (concentrate, manipulate)

**Effect** You fling the *eternal eruption*, with the effect of *[[Frozen Lava of Mhar Massif]]*. After 2d4 hours, the *eternal eruption* reforms itself in a container on your person, typically the one you most recently stored it in.

*Eternal Eruption of Mhar Massif* deals @Damage[11d6[fire]|options:area-damage] on a DC 30 [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
