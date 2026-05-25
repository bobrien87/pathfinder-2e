---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]"]
price: "{'gp': 1900}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This broom has a tenuous connection to gravity, and it tends to drift even while stowed. You can ride on the broom using one hand to guide it, and the broom can carry up to one passenger in addition to you.

The broom moves at a fly Speed of 20 feet. The broom can carry only so much, taking a –10-foot penalty to its Speed if laden with more than 20 Bulk, and crashing to the ground if it carries more than 30 Bulk.

**Activate—Lift Off** `pf2:2` (concentrate, manipulate)

**Effect** You name a destination on the same plane, and the broom speeds toward it at a fly Speed of 40 feet. You must either clutch the broom with two hands in order to ride it, or you need to release the broom to send it off with no rider. If you don't have a good idea of the location, layout, and general direction of the destination, or if your named destination is on another plane, the broom wanders aimlessly, circling back to its starting location after 30 minutes.

If the broom carries a rider, this activation lasts until 4 hours pass (typically 16 miles of travel), the broom reaches its destination, or you Dismiss the activation. If the broom doesn't have a rider, the activation lasts until the broom reaches its destination. When the activation ends, the broom floats to the ground and can't be activated again for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
