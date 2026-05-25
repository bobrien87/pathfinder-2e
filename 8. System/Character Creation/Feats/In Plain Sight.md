---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Alter Ego|Alter Ego]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Alter Ego Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

People often only see what they want to see, a weakness you know how to take full advantage of. While you've Assumed a Role, you can use Deception in place of Stealth when using the [[Avoid Notice]] exploration activity in an area where someone with your role wouldn't be unusual, such as when impersonating a sailor or fisher when infiltrating the docks.

**Source:** `= this.source` (`= this.source-type`)
