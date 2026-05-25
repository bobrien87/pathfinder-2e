---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Kitharodian Actor|Kitharodian Actor]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Kitharodian Actor Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You portrayed Grand Prince Stavian III in Fall of the Troubled King, a production dedicated to the life and times of the paranoid Taldan ruler whose violent resistance to new policies on succession kicked off the War for the Crown. Your acting won rave reviews for recasting Stavian's paranoia and political machinations in a sympathetic light, and you've learned to apply these subtle techniques outside of the stage to win others over. Whenever you succeed at a Deception or Performance check to portray a famous figure, you can select one creature within 60 feet who observed your performance. As long as this creature isn't hostile, its attitude toward you automatically improves by two steps (three steps if your check was a critical success). If it's hostile, it's [[Stupefied 2]] for 1 minute as it tries to reconcile its desire to harm you with its newfound sympathy for you.

**Source:** `= this.source` (`= this.source-type`)
