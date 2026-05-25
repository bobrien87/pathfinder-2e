---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Awakened animal]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Just as some humanoids find themselves driven to study nature, you are obsessed with the artificial constructs of society and can't get enough. You are trained in Society. If you would automatically become trained in Society, you instead become trained in a skill of your choice.

As a newcomer, sometimes your understanding is a bit off target. When you fail, but don't critically fail, a Society check to [[Recall Knowledge]] or [[Decipher Writing]], you learn the correct information (as you would on a success) and erroneous information (as you would on a critical failure). You don't have any way to differentiate which is which.

**Source:** `= this.source` (`= this.source-type`)
