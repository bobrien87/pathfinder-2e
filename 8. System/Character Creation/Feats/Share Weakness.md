---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Esoterica]]", "[[Manipulate]]", "[[Thaumaturge]]"]
prerequisites: "Exploit Vulnerability, mortal weakness"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are Exploiting a creature's Vulnerability using mortal weakness.

You select an object from your esoterica that has great personal value to you, such as a locket or treasured ring, and you grant it to an adjacent ally, establishing a personal link that allows your ally to affect an enemy as if they were you. The ally's Strikes apply the weakness from your mortal weakness the same way your Strikes do. This benefit ends when your [[Exploit Vulnerability]] ends or you Share Weakness again.

**Source:** `= this.source` (`= this.source-type`)
