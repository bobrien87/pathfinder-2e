---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sanguimancer|Sanguimancer]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Sanguimancer Dedication"
source: "Pathfinder #213: Thirst for Blood"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Cost** 1 or more sanguimancy Hit Points

You raise a defensive barrier of your own blood to protect you. You gain a +1 circumstance bonus to AC until the start of your next turn, increasing to a +2 bonus if you spend 10 or more sanguimancy Hit Points. While this bonus is in effect, you can use the Shield Block reaction with your blood shield. The blood shield has Hardness equal to four times the number of sanguimancy Hit Points you spent. After you use Shield Block, the blood shield dissipates, ending the circumstance bonus to AC early.

**Source:** `= this.source` (`= this.source-type`)
