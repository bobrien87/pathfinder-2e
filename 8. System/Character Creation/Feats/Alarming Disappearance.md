---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Minotaur]]"]
prerequisites: "expert in Stealth"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your ability to move unseen is startling for one your size, causing panic among your enemies. When you successfully [[Hide]] when previously observed, creatures you are [[Hidden]] from become [[Frightened]] 1. They are then temporarily immune to Alarming Disappearance for 1 hour. Typically, creatures that have traveled with you for a significant time, such as your fellow party members, are immune to your Alarming Disappearance.

**Source:** `= this.source` (`= this.source-type`)
