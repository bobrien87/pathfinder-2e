---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Twilight Talon|Twilight Talon]]"
source-type: "Remaster"
level: "7"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Twilight Talon Dedication, master in Deception"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're so familiar with the paperwork necessary to maintain your cover that you can easily whip up documents that support your fabrications. You can [[Create a Forgery]] using Deception, rather than Society, and doing so only takes 10 minutes, or 1 minute if you're legendary in Deception. With your paranoid nature, you're always on the lookout for forgeries. The GM rolls a secret Perception or Society check for you any time you encounter a forgery, even if you don't examine it closely.

**Source:** `= this.source` (`= this.source-type`)
