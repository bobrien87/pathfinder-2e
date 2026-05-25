---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Sorcerer]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature targets you with a spell of the same tradition as your bloodline.

The magic in your blood surges in response to your foe's spell. You generate a blood magic effect you know, even if you are already under the effects of blood magic. The target must be either you or the creature that triggered Blood Rising. If the blood magic effect grants you a bonus to AC or the appropriate saving throw, that bonus applies against the triggering spell. If the effect has a duration, it instead lasts until the beginning of your next turn.

**Special** This feat has the trait corresponding to the tradition of your bloodline.

**Source:** `= this.source` (`= this.source-type`)
