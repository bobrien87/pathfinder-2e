---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Attack]]", "[[Dragonblood]]"]
prerequisites: "expert in Athletics"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have a pair of draconic wings strong enough to batter your foes away and shove them away. Choose up to two creatures adjacent to you. Attempt an [[Athletics]] check and compare it to the Fortitude DC of each target. This counts as two attacks for your multiple attack penalty, but the penalty doesn't increase until after both attacks.
- **Critical Success** The target takes bludgeoning damage equal to double your level (@Damage[2*@actor.level[bludgeoning]]) and is pushed up to 10 feet away from you.
- **Success** The target takes bludgeoning damage equal to your level (@Damage[@actor.level[bludgeoning]]) and is pushed up to 5 feet away from you.
- **Failure** The target takes bludgeoning damage equal to half your level (@Damage[(floor(@actor.level/2))[bludgeoning]]).
- **Critical Failure** You fall [[Prone]] at the end of this activity.

**Source:** `= this.source` (`= this.source-type`)
