---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Auditory]]", "[[Bard]]", "[[Concentrate]]", "[[Spellshape]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your composition takes the form of a call-and-response chant that lets your allies continue the effect without you. If your next action is to cast a composition cantrip with a duration of 1 round, it becomes a call. While the spell is active, one ally of your choice affected by the spell can respond to your call as a single action that has the auditory and concentrate traits to extend the spell's duration by 1 round. Only one ally can respond to a given call, and responding to the ally's response has no additional effect.

**Source:** `= this.source` (`= this.source-type`)
