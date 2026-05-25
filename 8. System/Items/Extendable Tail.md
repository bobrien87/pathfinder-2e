---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Mechanical]]"]
price: "{'gp': 10}"
usage: "worn"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Built with collapsible poles and expanding hoops, this tail can extend to a length of 20 feet. While it's no more prehensile than a tail of a typical member of your ancestry, it ends with an anchor that you can secure around a sturdy object with an Interact action. While the tail is anchored, you can't move more than 20 feet from that spot, but you can use the tail to lower yourself up to 20 feet, as if it were a length of rope. You can use another Interact action to disengage the anchor and retract your tail.

**Source:** `= this.source` (`= this.source-type`)
