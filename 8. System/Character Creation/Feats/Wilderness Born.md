---
type: feat
source-type: "Remaster"
level: "1"
prerequisites: "ardande trait, plant trait, or wood trait"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're at home in the wilderness and easily disappear into it. You gain a +1 circumstance bonus to [[Hide]] and [[Sneak]] in natural terrain, and a +1 circumstance bonus to [[Sense Direction]] in natural terrain. While in natural terrain, you're always considered to be [[Covering Tracks]], even if you chose a different activity in exploration mode.

**Special** This feat gains the trait for your ancestry.

**Source:** `= this.source` (`= this.source-type`)
