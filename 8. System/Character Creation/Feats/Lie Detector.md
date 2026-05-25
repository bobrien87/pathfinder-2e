---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Investigator]]"]
prerequisites: "empiricism or interrogation methodology"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're adept at noticing the tells of a liar—sweat, flushing, a quavering voice, a quickening pulse. You gain a +1 circumstance bonus to Perception checks to [[Sense Motive]] and to Perception DCs against attempts to Lie to you. When you determine someone is lying to you, you can use their deceit to your advantage to gain a +1 circumstance bonus to the next Deception, Diplomacy, Intimidation, or Performance check you attempt against that creature within the next minute.

If you would gain your Pursue a Lead investigation bonus to any of the above checks, that bonus increases by 1 instead of you gaining the +1 bonus listed.

**Source:** `= this.source` (`= this.source-type`)
