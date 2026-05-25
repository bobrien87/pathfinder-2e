---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Investigator]]"]
prerequisites: "Thorough Research"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You fundamentally understand everything to the point where your research can't possibly be wrong. You are permanently [[Quickened]] and can use the extra action to [[Recall Knowledge]]. In addition, you gain the following benefits with Recall Knowledge.

- Your checks to Recall Knowledge are no longer secret.
- When you Recall Knowledge, you use the outcome for one degree of success better than the result of your check.
- If an effect (such as [[Dubious Knowledge]]) would give you inaccurate information from your Recall Knowledge check, you know which information is inaccurate.
- When one of your allies Recalls Knowledge and gains false information, you also know that information is inaccurate if they share it with you

**Source:** `= this.source` (`= this.source-type`)
