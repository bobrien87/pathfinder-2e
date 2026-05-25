---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Spellshot|Spellshot]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]", "[[Teleportation]]"]
prerequisites: "Spellshot Dedication, master in Arcana"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a loaded magical firearm or crossbow.

You merge your body with your ammunition, enabling you to travel the same path as your bolt or bullet. Strike a creature with the required weapon. On a success, if the target was within 120 feet, you and all your gear are teleported to an open space of your choice within 10 feet of the target.

**Source:** `= this.source` (`= this.source-type`)
