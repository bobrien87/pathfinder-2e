---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Blackjacket|Blackjacket]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Concentrate]]"]
prerequisites: "Mercenary Motivation"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have an active course of action planned.

When you're on a job, you can't allow anyone to stop you. Designate a single creature you can see as being an impediment to your active course of action. The first time you Strike your impediment in a round, you deal an extra die of weapon damage. At 14th level, this increases to two extra dice, and at 20th level, this increases to three extra dice.

You can have only one creature designated as an impediment at a time. If you use Nothing Personal against a creature when you already have a creature designated, the prior creature loses the designation, and the new impediment gains the designation. Otherwise, your designation lasts for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
