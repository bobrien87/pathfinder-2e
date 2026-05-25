---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Jotunborn]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've learned to fully move across planes, beginning with the Ethereal Plane. You can cast [[Interplanar Teleport]] twice per week as an occult innate spell that can target only yourself. Your body serves as the locus for the spell and allows you to travel between the Ethereal Plane, the Universe, or the space between the planes known as the Fray without needing a planar key. You can use these castings to travel to other planes if you have the appropriate planar keys, as normal.

**Source:** `= this.source` (`= this.source-type`)
