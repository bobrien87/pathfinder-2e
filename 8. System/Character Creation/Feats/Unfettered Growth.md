---
type: feat
source-type: "Remaster"
level: "13"
prerequisites: "ardande trait, plant trait, or wood trait"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

By tapping into the limitless power of the Plane of Wood, you can experience sudden, dramatic growth for a short time. Select one of the following benefits when you gain this feat. This choice is permanent and can't be changed.

- You gain 2nd-rank [[Enlarge]] as a primal innate spell. You can cast this spell twice per day and must target yourself. The spell's duration is 30 minutes.

- You gain 4th-rank *enlarge* as a primal innate spell. You can cast this spell once per day and must target yourself.

**Special** This feat gains the trait for your ancestry.

**Source:** `= this.source` (`= this.source-type`)
