---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Tattooed Historian|Tattooed Historian]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]"]
prerequisites: "Tattooed Historian Dedication"
source: "Pathfinder #207: The Resurrection Flood"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You critically fail a Diplomacy, Intimidation, or Performance check.

Orcs across Belkzen recognize you as an honored lorekeeper. You're adept at leveraging this status and showing off your tattoos to resolve conflicts, change minds, or distract others from a faux pas. You get a failure on the check, rather than a critical failure. If the triggering check was made against a creature with the orc trait, you can instead add the fortune trait to this ability and reroll the check, treating any critical failure as a failure.

**Source:** `= this.source` (`= this.source-type`)
