---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Auditory]]", "[[Bard]]", "[[Concentrate]]", "[[Spellshape]]"]
prerequisites: "warrior muse, Rallying Anthem"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Like the storied heroes who persist in the face of overwhelming odds, you and your allies will hold the line. If your next action is to cast the [[Rallying Anthem]] composition cantrip, you can Raise a Shield, and one ally of your choice who gains a status bonus from the spell can immediately use their reaction to Raise a Shield.

**Source:** `= this.source` (`= this.source-type`)
