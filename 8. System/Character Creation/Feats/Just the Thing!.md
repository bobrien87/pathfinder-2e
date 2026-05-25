---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Inventor]]"]
frequency: "once per PT1H"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

Need to balance on a razor's edge, force open an iron door, or persuade a dragon to negotiate? Never fear! No matter the situation, you always have just the thing. You attempt a skill action that takes 1 minute or less to complete, using the same number of actions or amount of time as normal. However, as you take the action, describe a device you pull out and use to accomplish the skill. The specifics of how you accomplish this are up to you, but they should fit the challenge at hand. For instance, you might use gravitic stabilizers to balance on the razor's edge, a force battering ram gizmo to open the iron door, or a device that produces an aroma with the ability to pacify wyrms to persuade the dragon. Using an invention in this way lets you alter how you calculate the skill check used in the action. Instead of the normal skill modifier associated with that skill action, you use your Crafting modifier.

**Source:** `= this.source` (`= this.source-type`)
