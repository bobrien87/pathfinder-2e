---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Choose an ally you can see, who becomes your designated ally. For the next minute, whenever your designated ally is adjacent to you and you're conscious, they gain a +2 circumstance bonus to AC and Reflex saving throws. You can have only one designated ally at a time, and if you designate a new ally, the previous ally loses any benefits.

> [!danger] Effect: Designate Ally

**Source:** `= this.source` (`= this.source-type`)
