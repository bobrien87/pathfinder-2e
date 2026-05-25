---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Thaumaturge]]"]
prerequisites: "Charisma +3"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Magical equipment and gear are the tools of your trade, and you know you need as many as possible to help you against the supernatural. Thus, mastering the efficient use of such magical equipment is a matter of great importance. You gain the Incredible Investiture skill feat, increasing your limit on invested items from 10 to 12. The limit increases to 14 if you have Charisma +4, 16 if you have Charisma +5, 18 if you have Charisma +6, and 20 if you have Charisma +7.

**Source:** `= this.source` (`= this.source-type`)
