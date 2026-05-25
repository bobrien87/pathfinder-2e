---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Fortune]]", "[[Investigator]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your most recent action was to [[Feint]], [[Request]], or [[Demoralize]], and you failed but didn't critically fail.

After your attempt to influence someone goes poorly, you add another bit of information or ask a pointed question, possibly salvaging your previous attempt. Reroll the failed check and use the new result. If the target of the failed check is involved with one of your active investigations, double your investigation bonus from [[Pursue a Lead]] on the rerolled check. That creature is temporarily immune to Just One More Thing for 1 day.

You can also use this action if you failed, but didn't critically fail, at a check to [[Lie]], [[Gather Information]], [[Make an Impression]], or [[Coerce]]. In this case, rather than spending 1 action, adding Just One More Thing takes you half the amount of time you initially spent on the check, to a minimum of 1 more round.

**Source:** `= this.source` (`= this.source-type`)
