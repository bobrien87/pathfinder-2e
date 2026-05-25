---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Automaton]]"]
prerequisites: "warrior automaton"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a creature [[Grabbed]] or [[Restrained]].

You channel magical power from your core into your arm, empowering your attack as you attempt to slam your foe into the ground. Attempt an [[Athletics]] check against the foe's Fortitude DC. You take a –2 circumstance penalty to your check if the target is one size larger than you and a –4 circumstance penalty if it's larger than that. You gain a +2 circumstance bonus to your check if the target is one size smaller than you and a +4 circumstance bonus if it's smaller than that.
- **Critical Success** You slam the foe down and the magical energy overwhelms it. The creature is knocked [[Prone]], becomes [[Dazzled]] for 1 round, and takes damage equal to 2d6 plus your Strength modifier. The foe is no longer [[Grabbed]] or [[Restrained]] by you.
- **Success** You slam the foe down. The creature is knocked prone and takes damage equal to your Strength modifier. The foe is no longer grabbed or restrained by you.
- **Failure** You are unable to slam the creature, but your hold on the creature remains.
- **Critical Failure** The creature breaks free and is no longer grabbed or restrained by you.

**Enhancement** Your arms better channel your core's power. You no longer take penalties for attempting to slam larger foes. Your foe takes damage equal to 2d6 plus your Strength modifier on a success (or double that on a critical success).

**Source:** `= this.source` (`= this.source-type`)
