---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "expert in Deception"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have a specific disguise that you keep at the ready, worn underneath your outer garment. You can change into this disguise to Impersonate as a 3-action activity. If you are a master in Deception, it is instead a 2-action activity, and if you are legendary in Deception, it is a single action. You can create a new backup disguise by spending the normal amount of time it takes you to Impersonate, but you can have only one backup disguise at a time. Having a backup disguise doesn't allow you to remove your armor or any other complex piece of clothing any more quickly, but once you have those off, the disguise is readily available. Because you have the backup disguise at the ready, it's possible that a thorough search might reveal some elements of the disguise (see Conceal an Object in the Stealth skill).

**Source:** `= this.source` (`= this.source-type`)
