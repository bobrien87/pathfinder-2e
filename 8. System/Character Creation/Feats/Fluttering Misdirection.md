---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Fan Dancer|Fan Dancer]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Fan Dancer Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've trained in drawing the eyes of your audience to specific aspects of your performance through the careful manipulation of your fans and body. While wielding a fan, you can snap open, flutter, or otherwise manipulate the fan to briefly distract observers around you, giving you and adjacent allies a constant +1 circumstance bonus to Stealth checks to secretly [[Conceal an Object]] and to Thievery checks to [[Steal]] or [[Palm an Object]].

**Source:** `= this.source` (`= this.source-type`)
