---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ulfen Guard|Ulfen Guard]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Fortune]]"]
prerequisites: "Ulfen Guard Dedication"
frequency: "once per PT10M"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

**Trigger** You fail a saving throw against an effect that has the mental trait.

When your enemies try to turn your mind against you, thoughts of your anathema bolster you. You can reroll the triggering saving throw with a +2 circumstance bonus, but you must use the new result, even if it's worse.

**Source:** `= this.source` (`= this.source-type`)
