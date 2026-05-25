---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Archfiend|Archfiend]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]"]
prerequisites: "Archfiend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your sheer determination has created a demiplane that houses a grand residence which will serve as the heart of your planned realm. You determine the appearance of this seat of power, such as a duskwood longhouse, a crumbling stone castle, an ice tower, or a pagoda constructed from the solidified souls of the damned.

You can enter your realm using the [[Enter Seat Of Power]] activity. You and any creatures you choose gain three times as many Hit Points when resting within your seat of power. Once per day while within your seat of power, you can cast [[Cleanse Affliction]] as a 4th-rank innate divine spell or [[Sound Body]] as a 4th-rank innate divine spell. You can target only yourself with these spells.

**Source:** `= this.source` (`= this.source-type`)
