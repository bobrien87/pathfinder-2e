---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mind Smith|Mind Smith]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Concentrate]]"]
prerequisites: "Mind Smith Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You temporarily change your weapon's shape to assist you in the field. You morph your weapon into a single simple tool, such as a shovel or crowbar, to help with a mundane task. You can't replicate entire toolkits with this ability. You can use this action again to change your mind weapon back to a weapon.

**Source:** `= this.source` (`= this.source-type`)
