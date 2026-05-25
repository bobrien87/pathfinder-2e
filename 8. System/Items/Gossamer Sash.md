---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Illusion]]", "[[Magical]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 1 hour (envision, Interact, move)

This lightweight sash of spidersilk measures 20 feet long when fully unfurled. White at one end and shading to violet at the other, occult markings in silver thread are stitched along the sash's length. When a gossamer sash is held by up to 4 people and they spend 1 hour walking along any road in Shenmen between midnight and sunrise, they step into an immersive mindscape that appears to be a lonely mountainside road inhabited by path maidens who are (at least initially) favorably disposed toward answering questions the travelers might have. Once the path maidens have answered their questions or are slain (whichever comes first), the mindscape ends, and those who traveled it are returned to the point on the road where they first activated the gossamer sash.

**Source:** `= this.source` (`= this.source-type`)
