---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Iridian Choirmaster|Iridian Choirmaster]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Fortune]]"]
prerequisites: "Iridian Choirmaster Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You and your student react as one to common threats. When you and your student are both targeted by the same effect that requires a Reflex saving throw, you and your student take the better of each of your die rolls for the save. You each still add your own Reflex save modifier to the die result.

**Source:** `= this.source` (`= this.source-type`)
