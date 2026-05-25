---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Fan Dancer|Fan Dancer]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Fan Dancer Dedication, Twirling Strike"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a fan.

You're practiced in using your fans to spin with dizzying speed. [[Tumble Through]] an opponent's space, and then Strike that opponent. If both the Tumble Through and Strike are successful, the opponent is [[Off Guard]] to the next attack made against it before the start of your next turn, and you can attempt to Tumble Through the space of a different opponent and Strike again with the same effect. If this second Tumble Through and Strike are successful, you can repeat these actions a third time against a third opponent.

**Source:** `= this.source` (`= this.source-type`)
