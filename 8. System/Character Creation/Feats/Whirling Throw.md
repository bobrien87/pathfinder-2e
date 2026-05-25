---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Attack]]", "[[Monk]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a creature [[Grabbed]] or [[Restrained]].

You propel your enemy away. Attempt an [[Athletics]] check against the foe's Fortitude DC. You take a –2 circumstance penalty to your check if the target is one size larger than you and a –4 circumstance penalty if it's larger than that. You gain a +2 circumstance bonus to your check if the target is one size smaller than you and a +4 circumstance bonus if it's smaller than that.
- **Critical Success** You throw the creature any distance up to 10 feet, plus 5 feet × your Strength modifier (`r 10+(5*@actor.abilities.str.mod)` feet). It takes bludgeoning damage equal to your Strength modifier plus 1d6 per 10 feet you threw it (@Damage[((floor((10+(5*@actor.abilities.str.mod))/10))d6 + @actor.abilities.str.mod)[bludgeoning]] damage). If you threw the target at least 10 feet and into a solid obstacle, use the maximum distance you could have thrown it to calculate the damage. The creature falls [[Prone]].
- **Success** As critical success, but the creature doesn't fall prone.
- **Failure** You don't throw the creature.
- **Critical Failure** You don't throw the creature, and it's no longer [[Grabbed]] or [[Restrained]] by you.

**Source:** `= this.source` (`= this.source-type`)
