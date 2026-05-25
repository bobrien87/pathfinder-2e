---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Companion]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 330}"
usage: "wornsaddle"
bulk: "4"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This saddle is covered with well-polished metal plates on the outside and adjusts to fit any mount.

**Activate—Ready for Battle** `pf2:2` (manipulate)

You touch the metal plates of the saddle, which begin to unfold around the creature, covering your mount in heavy barding that extends from a simple-looking saddle. The Bulk of the saddle is the same in either form, but your mount isn't affected by the restrictions or the benefits of wearing barding while it's in saddle form. If the mount is already wearing barding, this has no effect. You return the barding to saddle form by using the same activity.

**Source:** `= this.source` (`= this.source-type`)
