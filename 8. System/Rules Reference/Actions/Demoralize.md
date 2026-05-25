---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

With a sudden shout, a well-timed taunt, or a cutting put-down, you can shake an enemy's resolve. Choose a creature within 30 feet of you who you're aware of. Attempt an Intimidation check against that target's Will DC. If the target doesn't understand the language you are speaking, or you're not speaking a language, you take a –4 circumstance penalty to the check. Regardless of your result, the target is temporarily immune to your attempts to Demoralize it for 10 minutes.
- **Critical Success** The target becomes [[Frightened]] 2.
- **Success** The target becomes [[Frightened]] 1.

**Source:** `= this.source` (`= this.source-type`)
