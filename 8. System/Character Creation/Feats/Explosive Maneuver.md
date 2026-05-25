---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Inventor]]"]
prerequisites: "weapon innovation"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action was a successful Strike against a foe using your weapon innovation.

Thanks to a hidden experimental feature you built into your weapon, your weapon explosively deploys levers, tangling hooks, or similar mechanisms to provide significant assistance when you perform a combat maneuver. When you use Explosive Maneuver, choose Grapple, Shove, or Trip. Your weapon innovation must have a weapon trait that matches the action you chose (for instance, to choose Grapple, your weapon must have the grapple trait). You take the chosen action against the same foe as your previous successful Strike, using the same multiple attack penalty as your previous successful Strike. You still increase your multiple attack penalty after the Grapple, Shove, or Trip, as normal.

**Source:** `= this.source` (`= this.source-type`)
