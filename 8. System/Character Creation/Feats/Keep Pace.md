---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Game Hunter|Game Hunter]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Bounty Hunter Dedication or Game Hunter Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** Your prey is within reach and attempts to move away from you.

**Bounty Hunter** Once you are upon your prey, they can't escape.

**Game Hunter** When your hunted prey tries to bolt, you follow.

[[Stride]] up to your Speed, following the foe and keeping it in reach throughout its movement until it stops moving or you've moved your full Speed. You can use Keep Pace to [[Burrow]], [[Climb]], [[Fly]], or [[Swim]] instead of Stride if you have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
