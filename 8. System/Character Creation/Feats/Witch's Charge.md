---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Detection]]", "[[Witch]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You forge a magical link with another creature, granting you awareness of that creature's condition and creating a conduit for spellcasting. During your daily preparations, you can designate one willing creature as your charge. You are always aware of your charge's direction from you, its distance from you, and any conditions affecting it. In addition, you can cast spells with a range of touch on your charge from a range of 30 feet. These effects persist until your next daily preparations.

**Special** This feat has the trait corresponding to the tradition of spells you cast (arcane, divine, occult, or primal).

**Source:** `= this.source` (`= this.source-type`)
