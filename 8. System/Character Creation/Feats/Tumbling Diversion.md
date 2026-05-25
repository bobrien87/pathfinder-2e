---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Kobold]]"]
prerequisites: "expert in Acrobatics and Deception"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Attempt to [[Tumble Through]] an opponent's space. If you succeed or critically succeed and don't end your movement adjacent to that opponent, you can attempt to [[Create a Diversion]] to distract that opponent. You gain a +1 circumstance bonus to the Deception check (or a +2 circumstance bonus if you critically succeeded at the Acrobatics check to Tumble Through) to Create a Diversion. If you succeed or critically succeed to Create a Diversion, you become [[Hidden]] to only the creature whose space you Tumbled Through.

**Source:** `= this.source` (`= this.source-type`)
