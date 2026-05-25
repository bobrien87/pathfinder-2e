---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 10 minutes (manipulate)

This pale-blue ink dries rapidly, becoming fully transparent 1 minute after application. The ink glows red when exposed to heat, such as that from a torch or other open flame. This glow lasts only as long as the ink is exposed to heat, after which the ink becomes [[Invisible]] again. The crafter of the ghost ink can alter the formula slightly to instead make the ink sensitive to sunlight, starlight, magical light, or heatless light created by an alchemical effect, such as a [[Glow Rod]].

While the text isn't glowing, a creature closely examining a surface marked with ghost ink can detect the presence of the ink with a successful DC 25 [[Perception]] check. On a critical success, they can make out the ink well enough to use Society to [[Decipher Writing]]. One vial of ghost ink is sufficient to write a page worth of text.

**Source:** `= this.source` (`= this.source-type`)
