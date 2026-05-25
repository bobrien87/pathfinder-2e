---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Trapsmith|Trapsmith]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Trapsmith Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've learned how to build snares that trigger based on visual stimuli. When you construct a snare using gears, you can cause it to trigger based on the visual features of a creature. For example, you could lay a snare that can only be triggered by a Large or Larger creatures, or one that only activates when a creature wearing red clothing would trigger it. You can use this ability to specify your snares to trigger on creatures that typically do not trigger snares, such as creatures smaller than Small, though the creature must still otherwise satisfy the snare's trigger as normal.

**Source:** `= this.source` (`= this.source-type`)
