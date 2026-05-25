---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "master in Survival"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can Subsist using Survival on different planes, even those without resources or natural phenomena you normally need. For instance, you can forage for food without penalty even if the plane lacks food that could normally sustain you. A success on your check to Subsist also prevents damage done by the plane to you and anyone else you support with Subsist. This applies only to damage dealt by the general conditions of the plane, not smaller hazards.

**Source:** `= this.source` (`= this.source-type`)
