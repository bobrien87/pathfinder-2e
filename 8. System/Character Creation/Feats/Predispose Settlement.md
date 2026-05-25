---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Field Propagandist|Field Propagandist]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Downtime]]", "[[Skill]]"]
prerequisites: "Field Propagandist Dedication, expert in Deception"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You spend 7 days of downtime seeding propaganda through a settlement with a population of 2,500 or fewer. At 10th level, this increases to a settlement with a population of 10,000 or fewer, and at 16th level, you can affect settlements of any size.

Select a faction or organization (such as the Pathfinder Society, the Hellknights, or the Firebrands) that this propaganda targets and whether you are improving or decreasing the settlement's attitude toward that faction. After this period, attempt a [[Deception]] check or [[Diplomacy]] check against the hard DC of the level of the settlement. These changes last for 1 week before the people return to their original attitudes.
- **Critical Success** You adjust the starting attitude of the settlement's inhabitants toward the targeted faction by two steps. In addition, you gain a +1 circumstance bonus on initiative rolls made in encounters that include members of your targeted faction while in the settlement for 1 week.
- **Success** As critical success, but the inhabitants' attitude is adjusted by one step.
- **Critical Failure** The propaganda attempt backfires. The attitude of the settlement's inhabitants toward you decreases by one step.

**Source:** `= this.source` (`= this.source-type`)
