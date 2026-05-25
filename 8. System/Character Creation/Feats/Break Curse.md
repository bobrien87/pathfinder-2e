---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Exploration]]", "[[Healing]]", "[[Skill]]"]
prerequisites: "master in Occultism or Religion"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You spend 8 hours praying or performing occult rites over the target, weakening a curse's power over them. Attempt to counteract the curse, using [[Occultism]] check or [[Religion]] check for your counteract check and half your level rounded up for the counteract rank. Break Curse only takes 10 minutes of prayer and rites if you are legendary in Occultism or Religion.

**Source:** `= this.source` (`= this.source-type`)
