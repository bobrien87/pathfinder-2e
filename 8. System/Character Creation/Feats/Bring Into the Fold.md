---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Broken Chain|Broken Chain]]"
source-type: "Remaster"
level: "16"
traits: ["[[Auditory]]", "[[Emotion]]", "[[Linguistic]]", "[[Mental]]", "[[Mythic]]"]
prerequisites: "Broken Chain Dedication"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Not all who oppress are irredeemable, and given encouragement and some time, they will abandon their cause and join your fight against the very system they used to uphold. If your next action is to issue an [[Ultimatum of Liberation]], you may have up to 10 targets who can hear you attempt a [[Will]] save against your class DC or spell DC, whichever is higher. You can cause any changes in attitude to last longer than the current social interaction by spending at least 10 minutes speaking with the affected targets earnestly about your cause.
- **Success** The target is unaffected.
- **Failure** The target's attitude toward you improves by one step.
- **Critical Failure** The target's attitude toward you improves by two steps.

**Source:** `= this.source` (`= this.source-type`)
