---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Archaeologist|Archaeologist]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Fortune]]"]
prerequisites: "Archaeologist Dedication"
frequency: "once per PT1H"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Trigger** You fail a check against a trap, such as a Thievery check to [[Disable]] the trap or a Reflex save to avoid its effects.

You are more than just skillful; your drive to find the secrets of the past manifests as a strange kind of luck. Reroll the failed check and use the new result.

**Source:** `= this.source` (`= this.source-type`)
