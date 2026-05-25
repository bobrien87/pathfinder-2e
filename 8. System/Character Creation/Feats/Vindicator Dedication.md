---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Vindicator|Vindicator]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Class]]", "[[Dedication]]"]
prerequisites: "Vindicator"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your church ensures that you are cared for. You can use Religion to Coerce, Gather Information, Make an Impression, or Request as long as you are in a town or city with a church dedicated to your deity. If the target of the check is also a worshipper of your deity or is your hunted prey, you gain a +2 circumstance bonus to the check.

Vindicator

**Source:** `= this.source` (`= this.source-type`)
