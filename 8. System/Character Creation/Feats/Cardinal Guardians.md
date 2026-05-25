---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Animist]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You focus your divine magic to allow your apparitions to work in concert using the magic from one to weaken an enemy against the power of the next. Whenever you succeed at a spell attack with an apparition spell or vessel spell, or when a creature fails its save against such a spell, you gain a +2 status bonus to your spell attack modifier against that creature with spells granted by any of your other apparitions, and it takes a –2 status penalty to its saves against such spells. These benefits last until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
