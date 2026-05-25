---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** Member of the Bellflower Network

This mug looks like any other; however, the bottom part unscrews to reveal a velvet-lined chamber. These are primarily used by members of the Bellflower Network to sneak messages and small objects to other possible members. The Perception DC to discover the false bottom is 15 if someone specifically examines the mug.

**Source:** `= this.source` (`= this.source-type`)
