---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Blackjacket|Blackjacket]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Exploration]]"]
prerequisites: "Blackjacket Dedication"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A large part of being in the Mercenary League entails doing mercenary work. You spend 1 minute planning a course of action that will allow you to complete a task you've been hired or requested to do. Work with your GM to determine the circumstances of any job or task if need be, but typically, they can involve protecting a place or person, defeating a foe or enemy force, or retrieving an item. The course of action you plan must be something you believe you can accomplish.

**Active Plan** You can have only one course of action planned at a time. If you use Mercenary Motivation to plan a second course of action, you no longer receive the bonus to checks related to the first course of action.

**On the Job** Whenever you attempt a Perception check or skill check that will advance your course of action, you gain a +1 circumstance bonus to the check. The exact checks this bonus applies to depend on your current job and are determined by the GM.

**Finishing a Plan** When you complete the course of action you planned to do, you don't lose the bonus or other benefits until you make a different plan with Mercenary Motivation or voluntarily Dismiss the current plan.

**Source:** `= this.source` (`= this.source-type`)
