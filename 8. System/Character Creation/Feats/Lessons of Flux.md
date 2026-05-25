---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Fortune]]", "[[Monk]]"]
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Trigger** You fail a skill check to [[Grapple]], [[Reposition]], [[Shove]], [[Trip]], or [[Tumble Through]].

You apply the persistence and permutation taught by faydhaans to your failures. You reroll the check and take the second result. If it still fails or critically fails, you can ask a question about the creature you were attempting to Grapple, Reposition, Shove, Trip, or Tumble Through as if you had succeeded at a check to [[Recall Knowledge]].

**Source:** `= this.source` (`= this.source-type`)
