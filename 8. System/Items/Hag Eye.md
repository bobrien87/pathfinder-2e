---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Occult]]", "[[Scrying]]"]
price: "{'gp': 50}"
usage: "worn"
bulk: "—"
source: "Pathfinder Monster Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This item appears to be an ordinary semiprecious stone and is typically mounted on a brooch or ring, but the stone is, in fact, an eyeball. This illusion can be seen through with [[Truesight]] or similar magic, and anyone who interacts with the item feels its wet, sticky surface, allowing them to attempt to disbelieve the illusion (DC 19 [[Perception]] check). Many hags claim a hag eye is more effective if plucked from a living, awake creature, but this is likely just a convenient excuse for sadism.

The hag eye produces no direct benefit for the wearer, but allows the hag who created it, or any member of their coven, to peer through the eye using the [[Seek]] action. This has no range limit, provided the hag is on the same plane.

Any damage dealt to the eye destroys it. If this happens while a hag is looking through it, the hag is [[Blinded]] for 1 hour.

**Craft Requirements** You are a hag.

**Source:** `= this.source` (`= this.source-type`)
