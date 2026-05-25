---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pistol Phenom|Pistol Phenom]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Pistol Phenom Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your tricks discombobulate your opponent, leaving spots in their vision from the bright flash of your gunshot reflected straight into their eyes (or other visual organs). Attempt a Performance check against the target creature's Will DC and make a ranged firearm Strike against that target. If the Strike deals damage to the target creature and you succeed at the Performance check, the creature is [[Dazzled]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
