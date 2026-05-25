---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Chronoskimmer|Chronoskimmer]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Fortune]]"]
prerequisites: "Chronoskimmer Dedication"
frequency: "once per day"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** You fail a skill check or saving throw.

After failing a test of skill, you hop back in your personal timeline so you can try again. You reroll the triggering check with a +1 circumstance bonus as you apply your experience from your last attempt. You must use the new result, even if it's worse than your first roll.

**Source:** `= this.source` (`= this.source-type`)
