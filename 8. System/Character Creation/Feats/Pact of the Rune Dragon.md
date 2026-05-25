---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pactbinder|Pactbinder]]"
source-type: "Remaster"
level: "16"
traits: ["[[Arcane]]", "[[Archetype]]"]
prerequisites: "Pactbinder Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

While the students of Cobyslarni are taught to make pacts with many kinds of dragons, a pact with a rune dragon is somewhat more frequent due to their interest in the accomplishments of various academies. You immediately learn 10 languages chosen from common languages, uncommon languages, and any others the dragon has access to. Additionally, you can Identify Magic at a range of 30 feet as a single action ability with the concentrate trait.

In exchange, the rune dragon requires you to research a topic and send a detailed report each year. Year to year, the dragon may change the interest of your research as they see fit. If you fail to send an appropriately detailed report, you lose this ability unless you spend one week serving the dragon.

**Source:** `= this.source` (`= this.source-type`)
