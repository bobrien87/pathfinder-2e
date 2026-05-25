---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Starstone Aspirant|Starstone Aspirant]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Flourish]]", "[[Press]]"]
prerequisites: "Starstone Aspirant Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

So many other hopefuls have attempted the Test of the *Starstone* before you and failed. Whether they were killed or disappeared, you vow to honor their memories by succeeding where they failed. This drive allows to push forward after you've already made an attack. You Step and then Strike.

**Source:** `= this.source` (`= this.source-type`)
