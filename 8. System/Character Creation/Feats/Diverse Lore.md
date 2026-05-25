---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Thaumaturge]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your wandering studies mean you've heard rumors or theories about almost every topic... though admittedly, your sources aren't always the most reliable. You can take a -2 penalty to your check to Recall Knowledge with Esoteric Lore to Recall Knowledge about any topic, not just the usual topics available for Esoteric Lore. Additionally, when you succeed at your check to Exploit a Vulnerability, compare the result of your Esoteric Lore check to the DC to Recall Knowledge for that creature; if that number would be a success or a critical success, you gain information as if you had succeeded at the Recall Knowledge check.

**Source:** `= this.source` (`= this.source-type`)
