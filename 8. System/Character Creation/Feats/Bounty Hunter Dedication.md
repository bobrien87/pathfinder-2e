---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Bounty Hunter|Bounty Hunter]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Survival"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When focused on finding your quarry, you're relentless. You gain the Hunt Prey action. You can use Hunt Prey to designate a creature that you've observed, heard about, or learned about through some other means, such as a bounty board or wanted poster. In addition to the other benefits of Hunt Prey, you can designate a target as your prey while Gathering Information about them, in addition to designating them as your prey when Tracking them as normal. If you have already identified your target and selected them as your prey, you gain a +2 circumstance bonus to checks to Gather Information about them.

If you already have Hunt Prey, you gain the Monster Hunter feat in addition to the other benefits of this feat.

Bounty Hunter

**Source:** `= this.source` (`= this.source-type`)
