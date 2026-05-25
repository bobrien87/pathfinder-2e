---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Guardian]]"]
prerequisites: "Hampering Stance"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature within your reach leaves a square during a move action it's using.

**Requirements** You are in [[Hampering Stance]].

You lash out when foes try to get past you, possibly stopping them in their tracks. Make a melee Strike against the triggering creature. The Strike gains the following additional results.
- **Critical Success** The target's movement is disrupted.
- **Success** The target takes a –10-foot circumstance penalty to its Speed for the rest of its triggering movement. This penalty might cause the triggering creature's movement to end immediately based on its affected Speed.
- **Failure** As success, but the target instead takes a –5-foot circumstance penalty to its Speed.
- **Critical Failure** The target is unaffected.

**Source:** `= this.source` (`= this.source-type`)
