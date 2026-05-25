---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Werecreature|Werecreature]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Visual]]"]
prerequisites: "Werecreature Dedication, you were afflicted with the curse of the werecreature"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your flesh tears and warps as you transform. Attempt Intimidation checks to [[Demoralize]] each enemy within 30 feet. This Demoralize loses the auditory trait and gains the visual trait, and you don't take a penalty if a creature doesn't understand your language. Regardless of the results of your checks, each creature is temporarily immune to Terrifying Transformation for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
