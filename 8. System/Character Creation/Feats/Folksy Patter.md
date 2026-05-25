---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Halfling]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are adept at disguising coded messages as folksy idioms. Using slang, jokes, halfling loanwords, and the like, you convey a simple message consisting of three basic words (such as "Danger assassin flee" or "Meet me moonrise"). Your intended listener can attempt a DC 20 [[Perception]] check to discern the message. This DC is reduced by 5 if the listener is a halfling or has Folksy Patter, or by 10 if both apply (DC 15 [[Perception]] check DC 10 [[Perception]] check). Eavesdroppers can also attempt a [[Perception]] check against your Deception DC to discern your meaning. Any bonuses or penalties to Perception checks to [[Sense Motive]] apply to checks to understand Folksy Patter.

**Source:** `= this.source` (`= this.source-type`)
