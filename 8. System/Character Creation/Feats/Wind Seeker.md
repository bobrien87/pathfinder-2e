---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Animist]]"]
prerequisites: "Walk the Wilds"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Wings free you from the shackles of the ground below. You add [[Aerial Form]] to your apparition spell repertoire, allowing you to cast it with your apparition spellcasting. Whenever you use *aerial form* to gain a form that grants you a specific Acrobatics modifier, you gain a +1 status bonus to Acrobatics checks.

**Special** If you are attuned to an apparition of darkened boughs, add the bat and bird forms in *aerial form* to your [[Darkened Forest Form]] lists.

**Source:** `= this.source` (`= this.source-type`)
