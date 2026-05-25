---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ascended Celestial|Ascended Celestial]]"
source-type: "Remaster"
level: "14"
traits: ["[[Concentrate]]", "[[Mythic]]"]
prerequisites: "Ascended Celestial Dedication"
frequency: "once per PT1H"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You embrace your divine spark, unleashing your full potential. Your nimbus automatically activates (if it isn't already) and the area of your nimbus doubles; you shed bright light for 60 feet (and dim light to the next 60 feet). You can't suppress your nimbus while Channeling your Divine Spark. You gain a number of temporary Hit Points equal to your level, and resistance to physical damage equal to half your level. You gain the [[Quickened]] condition and can use the extra action each round only for Strike and Stride actions. Each time that you damage a creature with a melee Strike, you can attempt to [[Shove]] or [[Trip]] that creature as a free action. These effects last for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
