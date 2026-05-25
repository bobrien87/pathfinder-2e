---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Reincarnated]]"]
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Reincarnation has given you a compassionate perspective and enabled you to relate to almost everyone you speak with, putting them at ease and quickly generating trust. Whenever you attempt a Diplomacy check to [[Make an Impression]] or [[Request]] something, the DC is reduced by 2, and if the creature you're speaking with is lower level than you, any success is a critical success. Whenever you attempt a Diplomacy check to [[Gather Information]], you can't critically fail.

**Source:** `= this.source` (`= this.source-type`)
