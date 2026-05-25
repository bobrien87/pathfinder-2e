---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Prophet Of Kalistrade|Prophet Of Kalistrade]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Prophet of Kalistrade Dedication"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know staying cool is key to prevailing in social situations, as anger leads to mistakes. When a creature you're interacting with decreases its attitude from indifferent to unfriendly or from unfriendly to hostile, you gain a +2 circumstance bonus to any attempts to [[Make an Impression]] on the creature for the next hour. If this decrease in attitude leads to combat, you gain a +1 circumstance bonus to the subsequent initiative roll instead.

**Source:** `= this.source` (`= this.source-type`)
