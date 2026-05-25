---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Time Mage|Time Mage]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Manipulate]]"]
prerequisites: "Time Mage Dedication"
frequency: "once per day"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You invest in two futures, then choose the one to make a reality. You Cast two Spells that each take 1 or 2 actions to cast. These can't be the same spell heightened to two different ranks. You expend the resources for both spells, such as spell slots, Focus Points, and costs, such as gp or valuables. Determine the immediate results for both spells, including attack rolls, saving throws, damage, and any other dice rolls. Then, choose which of the two spells takes effect, using the previously attempted rolls. The other spell's resources are still expended, but the spell has no effect as the magic disappears to the other timeline.

**Source:** `= this.source` (`= this.source-type`)
