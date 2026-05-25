---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Prophesied Monarch|Prophesied Monarch]]"
source-type: "Remaster"
level: "14"
traits: ["[[Incapacitation]]", "[[Mythic]]"]
prerequisites: "Prophesied Monarch Dedication"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You assume a demeanor of authority and decree banishment upon a foe who has defied your authority. Speak your decree; a creature you designate within 60 feet who can hear your decree must succeed at a Will saving throw against your class DC or spell DC (whichever is higher) or spend its next turn moving as far away from you as it possibly can; this includes using magic or special movement modes, if it has any, to expedite its retreat.

If the target attempts to move back within 60 feet of you at any time in the next week, it must succeed at a [[Will]] save saving throw against your class DC or spell DC (whichever is higher) or the attempt fails, any movement ends, and any actions or spell slots used in the attempt (such as if the target were attempting to magically approach you) are wasted.

When you speak a Decree of Banishment, you can spend 1 Mythic Point as part of the action to have all friendly creatures and even the land itself within a 10-mile radius of you at that moment to reject the banished target. Within the affected area for the next month, the target has a –4 penalty to all Diplomacy checks to Gather Information or [[Make an Impression]], all Intimidation checks to [[Coerce]], and all Survival checks to Subsist. If the target defies your Decree of Banishment and continues to operate within the area, you hear about their activities the next time you encounter a group of friendly creatures with 10 or more members. You can have only one target affected by this month-long banishment at a time; if you inflict a month-long banishment on another target, the effects on the first target end.

**Source:** `= this.source` (`= this.source-type`)
