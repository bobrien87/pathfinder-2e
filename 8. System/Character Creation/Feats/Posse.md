---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Bounty Hunter|Bounty Hunter]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Exploration]]"]
prerequisites: "Bounty Hunter Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have designated prey with Hunt Prey.

By spending 1 minute giving guidance to help hunt down your prey, you instruct up to five willing creatures to assist you. They gain a +1 circumstance bonus to [[Seek]] your prey, to [[Track]] your prey, and to [[Gather Information]] about your prey. You and the creatures assisting you gain a +1 circumstance bonus to initiative rolls when entering combat with your prey.

These benefits lasts until you designate a new prey or your prey dies, whichever comes first. An individual creature assisting you loses this benefit if they're out of your presence for too long to benefit from your instructions. This is usually 1 hour, but is determined by the GM.

**Source:** `= this.source` (`= this.source-type`)
