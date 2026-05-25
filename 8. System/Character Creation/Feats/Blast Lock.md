---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Gunslinger]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a loaded firearm.

Sometimes taking the shortest distance between two points involves removing an obstacle or two. You shoot your firearm at a lock within 10 feet. Make an attack roll against the DC required to [[Pick the Lock]]
- **Critical Success** You open the lock, or you achieve two successes toward opening a complex lock.
- **Success** You open the lock, or you achieve one success toward opening a complex lock.
- **Failure** You fail to open the lock, and your shot makes it harder to open. Future attempts to Pick the Lock or Blast the Lock take a -2 circumstance penalty.
- **Critical Failure** You fail to open the lock, and your shot makes it much harder to open. Future attempts to Pick the Lock or Blast the Lock take a -4 circumstance penalty.

**Source:** `= this.source` (`= this.source-type`)
