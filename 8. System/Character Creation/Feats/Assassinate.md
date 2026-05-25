---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Assassin|Assassin]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Assassin Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have designated a mark using [[Mark for Death]] and are completely unnoticed by your mark.

You strike with one swift movement, trying to instantly slay your mark. Make a Strike against your mark. If you hit, your mark takes an additional 6d6 precision damage with a [[Fortitude]] save against the higher of your class DC or spell DC. If the mark critically fails, it dies unless its level is higher than yours. Regardless of the result of its save, the creature is temporarily immune to your Assassinate for 1 day.

**Source:** `= this.source` (`= this.source-type`)
