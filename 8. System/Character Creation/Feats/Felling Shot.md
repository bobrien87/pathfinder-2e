---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Rogue]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your ranged attacks can shoot an unprepared foe right out of the air. Make a ranged Strike against an [[Off Guard]] creature. If the Strike is a success and deals damage, the target must attempt a [[Reflex]] save against your class DC.
- **Success** The target is unaffected.
- **Failure** The target falls up to 120 feet. If it hits the ground, it takes no damage from the fall.
- **Critical Failure** As failure, and the target can't fly, jump, levitate, or otherwise leave the ground until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
