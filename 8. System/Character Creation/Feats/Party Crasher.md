---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Dandy|Dandy]]"
source-type: "Remaster"
level: "7"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Dandy Dedication, master in Society"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You attend all the fashionable society parties, no matter how exclusive they might be.

Any time you encounter a social event you would ordinarily be denied access to, such as a coronation, royal gala, or other society function, you can spend `r 1d4` hours to secure entry without the need for a skill check. You find invitations, invitees looking for fashionable dates, temporary jobs with the caterers, event staff willing to look the other way, or some other mode of access for yourself and your allies.

This ability doesn't apply to secret events or other small private gatherings with no staff, dates, or outsiders involved.

**Source:** `= this.source` (`= this.source-type`)
