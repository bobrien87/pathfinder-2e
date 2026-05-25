---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Overwatch|Overwatch]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Overwatch Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you observe an ally try and fail to execute a strategic maneuver against your enemies, you coordinate with your other allies to finish the job, using the opening from the first attempt to keep your foe off-balance and ensure your eventual success.

When an ally within your overwatch field attempts to [[Disarm]], [[Shove]], or [[Trip]] an opponent within your overwatch field and fails, you coordinate efforts to provide a +2 circumstance bonus to the next Athletics check rolled by a different ally to attempt the same action on the same target before that target's next turn.

> [!danger] Effect: Topple Giants

**Source:** `= this.source` (`= this.source-type`)
