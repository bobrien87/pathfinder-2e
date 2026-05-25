---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Investigator]]"]
prerequisites: "empiricism methodology"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Sharp and piercing, your eyes see all and convey more. Your [[Point Out]] actions lose the auditory trait, and you don't need to be heard to convey the information to your allies. In addition, a creature you Point Out is [[Off Guard]] to your allies until the start of your next turn.

**Special** If you have the [[Blind Fight]] feat, your allies gain that feat's benefits against any creature that's off-guard due to Empiricist's Eye.

**Source:** `= this.source` (`= this.source-type`)
