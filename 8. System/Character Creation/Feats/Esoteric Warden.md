---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Thaumaturge]]"]
prerequisites: "Exploit Vulnerability"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you apply antithetical material against a creature successfully, you also ward yourself against its next attacks. When you succeed at your check to [[Exploit a Vulnerability]], you gain a +1 status bonus to your AC against the creature's next attack and a +1 status bonus to your next saving throw against the creature; if you critically succeed, these bonuses are +2 instead. You can gain these bonuses only once per day against a particular creature, and the benefit ends if you Exploit Vulnerability again.

**Source:** `= this.source` (`= this.source-type`)
