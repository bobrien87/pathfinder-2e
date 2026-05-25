---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sterling Dynamo|Sterling Dynamo]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]"]
prerequisites: "Sterling Dynamo Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've built clockwork wings or jets into your dynamo, allowing you to use your prosthesis to fly. You gain a fly Speed equal to your Speed. Each minute of flight reduces the operational time of your sterling dynamo by 1 hour, measured from the first time you use the Fly action in a given minute.

**Source:** `= this.source` (`= this.source-type`)
