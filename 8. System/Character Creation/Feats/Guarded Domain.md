---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beast Lord|Beast Lord]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Beast Lord Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You and your united companion have elected to become guardians of a particular location or domain. If you spend 1 week of downtime within a settlement or natural area with a 5-mile radius, you and your companion can become guardians of the area and consider it to be your guarded domain. Your guarded domain remains under your protection until you spend more than 1 month outside of your domain, after which you must spend another week of downtime to re-attune to your guarded domain. You can only have one guarded domain at a time, and selecting a new guarded domain immediately ends your protection over the previous guarded domain.

If a creature has been in your guarded domain for at least 1 hour while you or your companion are also inside your domain, you or your companion can attempt to [[Gather Information]] about the target by spending 1 minute communing with the land or its residents. You attempt this check at mythic proficiency.

In addition, once per day as a 3-action activity you can spend a Mythic Point to instantly teleport yourself and your united companion to a location you are aware of within your domain. This is a teleportation effect.

**Source:** `= this.source` (`= this.source-type`)
