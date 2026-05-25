---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Inventor|Inventor]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]", "[[Multiclass]]"]
prerequisites: "Intelligence +2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You become trained in Crafting and inventor class DC. You gain the [[Inventor]] skill feat, even if you don't meet the skill feat's requirements. Choose an innovation. You gain that innovation, though you don't gain any other abilities that modify or use that innovation, such as modifications or [[Explode]].

Inventor

**Source:** `= this.source` (`= this.source-type`)
