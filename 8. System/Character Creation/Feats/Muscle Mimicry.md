---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Alter Ego|Alter Ego]]"
source-type: "Remaster"
level: "7"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Skill]]"]
prerequisites: "Alter Ego Dedication, trained in Athletics, master in Deception"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An enemy makes a successful [[Disarm]], [[Escape]], [[Grapple]], [[Shove]], or [[Trip]] attempt.

Your study of another allows you to mirror their movements subtly, even in the heat of combat. You study the successful maneuver of an enemy and instinctively learn to do it. The next time you take the same action they did, you gain a +1 circumstance bonus to your Athletics check, or a +2 circumstance bonus if the enemy critically succeeded on their triggering action. You lose this benefit if you don't use it before the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
