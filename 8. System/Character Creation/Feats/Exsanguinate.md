---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sanguimancer|Sanguimancer]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Sanguimancer Dedication"
source: "Pathfinder #213: Thirst for Blood"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** On your last action, you dealt damage to a creature that isn't immune to bleed damage and is within 10 feet. The damage must have come from a piercing or slashing Strike. You must have succeeded at your attack roll, or the creature must have failed its saving throw, as applicable.

After one of your attacks, you direct your foe's blood to spray upon you, infusing you with life energy. You gain a number of sanguimancy HP equal to half your level that last only until the end of your next turn. Exsanguinate works only against active foes who are able to act and aren't [[Restrained]].

**Source:** `= this.source` (`= this.source-type`)
