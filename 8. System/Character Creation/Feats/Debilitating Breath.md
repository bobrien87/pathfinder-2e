---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Dragonblood]]"]
prerequisites: "Breath of the Dragon"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your breath causes lasting hindrance to those it harms. Creatures who fail their saves against your Breath of the Dragon gain one of the following conditions, based on the damage type of your breath: [[Clumsy]] 1 (electricity, cold, fire, or sonic damage), [[Enfeebled]] 1 (acid, physical, or poison damage), or [[Stupefied 1]] (force, mental, spirit, vitality, or void damage). The condition lasts until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
