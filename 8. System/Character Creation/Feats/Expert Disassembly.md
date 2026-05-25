---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Scrounger|Scrounger]]"
source-type: "Remaster"
level: "7"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "master in Crafting, Scrounger Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can apply the same techniques you use to reverse engineer objects to disable dangerous traps and break apart locks. You can use Crafting instead of Thievery to [[Disable a Device]] or [[Pick a Lock]].

`act pick-a-lock skill=crafting`

`act disable-device skill=crafting`

**Source:** `= this.source` (`= this.source-type`)
