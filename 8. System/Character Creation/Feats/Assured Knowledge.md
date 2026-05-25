---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Bard]]"]
prerequisites: "enigma muse"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can procure information with confidence. Whenever you [[Recall Knowledge]] using any skill (including Bardic Lore), you can forgo rolling your check to instead receive a result of 10 + your proficiency bonus (don't apply any other bonuses, penalties, or modifiers).

As long as you are an expert in a skill, you meet the prerequisites for the [[Automatic Knowledge]] skill feat in that skill, even if you don't have [[Assurance]] in that skill.

**Source:** `= this.source` (`= this.source-type`)
