---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Spellshot|Spellshot]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Magical]]", "[[Teleportation]]"]
prerequisites: "Spellshot Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You build a powerful magical connection with a chosen gun or crossbow. During your daily preparations, choose a single crossbow or firearm. Until your next daily preparations, you can use the [[Call Gun]] action to call the gun to your hand.

**Source:** `= this.source` (`= this.source-type`)
