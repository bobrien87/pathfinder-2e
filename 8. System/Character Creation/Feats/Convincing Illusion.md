---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Wizard]]"]
prerequisites: "expert in Deception"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature succeeded, but didn't critically succeed, at a Perception check or Will save to disbelieve an illusion from a spell that you cast.

**Requirements** You are within 30 feet of the observer and the illusion.

You use your deceptive skills to make your illusions seem even more real. Attempt a [[Deception]] check against the target's Perception DC. If you succeed, the target fails to disbelieve the illusion.

**Source:** `= this.source` (`= this.source-type`)
