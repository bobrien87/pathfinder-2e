---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Magaambyan Attendant|Magaambyan Attendant]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Uzunjati Recollection, legendary in a Recall Knowledge Skill"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your stories aren't mere tales passed down from elder to youth or teacher to student. They're the lived experiences of those you've met, and they're the stuff of legend. When you use [[Uzunjati Recollection]], if you're legendary in the skill you use to Recall Knowledge, you gain a +1 circumstance bonus to the Recall Knowledge check, and the circumstance bonus to [[Uzunjati Storytelling]] increases to +2.

**Source:** `= this.source` (`= this.source-type`)
