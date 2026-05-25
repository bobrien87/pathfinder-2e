---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Rogue]]"]
prerequisites: "legendary in Deception"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your deceptions confound even the most powerful magic that could spy on you. Detection, revelation, and scrying effects pass right over you, your possessions, and your auras, detecting nothing unless the detecting effect has a counteract rank of 10 or higher. For example, [[Detect Magic]] would still detect other magic in the area but not any magic on you, [[Truesight]] wouldn't reveal you, [[Locate]] or [[Scrying]] wouldn't find you, and so on.

**Source:** `= this.source` (`= this.source-type`)
