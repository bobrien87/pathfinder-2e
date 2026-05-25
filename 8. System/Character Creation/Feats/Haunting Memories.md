---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ghost|Ghost]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Headless Haunt"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your soul bears metaphysical impressions of the innumerable other spirits imprisoned with you in the [[Final Blade]] from which you escaped, allowing you to draw upon their memories. When you make your daily preparations, you can either gain the expert proficiency rank in one skill in which you're untrained or raise your proficiency rank to master in one skill in which you're trained or better. You also gain one skill feat with a minimum requirement of your new rank in the chosen skill. For the purpose of meeting level prerequisites for this feat, your level is equal to half your level.

This proficiency and feat last until you make your daily preparations again. Since the proficiency is temporary, you can't use it as a prerequisite for any permanent character option.

**Source:** `= this.source` (`= this.source-type`)
