---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Aftermath]]", "[[Magical]]"]
prerequisites: "You have succeeded at an important task given by a dragon such as procuring a special treasure for their hoard"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

In pleasing the cravings of a mighty dragon, they have deigned to impart some of their magical essence into your body. Your eyes begin to glow and change color while your limbs and neck grow a veneer of scales, visually matching the associated dragon, accompanied by a near-insatiable desire to amass a hoard of your own. You gain the [[Dragon Breath]] sorcerer bloodline spell, emulating the breath of the associated dragon. If you don't have one, you gain a focus pool of 1 Focus Point. You Refocus by counting and arranging your treasure.

**Source:** `= this.source` (`= this.source-type`)
