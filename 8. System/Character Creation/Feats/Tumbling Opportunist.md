---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Acrobat|Acrobat]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Attack]]"]
prerequisites: "Acrobat Dedication"
frequency: "once per PT1M"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

**Requirements** Your most recent action was to [[Tumble Through]] or [[Tumbling Strike]], and you successfully moved through an enemy's space.

You use a burst of stamina to perform a breathtaking feat of Acrobatics as you speed through a foe's space, leaving your foe lying flat on their back. You attempt to `act trip` the enemy whose space you moved through. You can use Acrobatics (`act trip skill=acrobatics`) instead of Athletics for this check.

**Source:** `= this.source` (`= this.source-type`)
