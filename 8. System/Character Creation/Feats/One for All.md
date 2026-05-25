---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Emotion]]", "[[Linguistic]]", "[[Mental]]", "[[Swashbuckler]]"]
prerequisites: "trained in Diplomacy"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With precisely the right words of encouragement, you bolster an ally's efforts. Designate an ally within 30 feet; this action counts as sufficient preparation to [[Aid]] that ally. When you use the Aid reaction to help that ally, you can roll [[Diplomacy]] check in place of the usual check and the action gains the bravado trait

**Source:** `= this.source` (`= this.source-type`)
