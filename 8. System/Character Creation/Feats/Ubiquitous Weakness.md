---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Manipulate]]", "[[Thaumaturge]]"]
prerequisites: "Share Weakness"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've nurtured your bonds with your comrades, allowing you to share the benefits of your esoterica. When you use [[Exploit Vulnerability]] and choose mortal weakness, select any number of allies within 30 feet of you. Their Strikes apply the weakness from mortal weakness the same way your Strikes do. This benefit ends when you stop benefiting from Exploit Vulnerability. Since this effect depends on magically strengthening your bond to your allies, only allies with whom you've developed a rapport over the course of one or more days gain the benefit.

**Source:** `= this.source` (`= this.source-type`)
