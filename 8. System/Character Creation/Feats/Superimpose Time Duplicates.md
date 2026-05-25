---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Chronoskimmer|Chronoskimmer]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Chronoskimmer Dedication"
frequency: "once per PT1H"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You call alternate versions of yourself, either from a different timeline or perhaps yourself from a different point in your current timeline, to aid you in combat. Until the start of your next turn, these alternate selves flicker in and out in your vicinity, providing flanking for you against all enemies within your reach. Flanking with your time duplicates is the same as flanking with an ally and so is subject to effects like all-around vision or the [[Deny Advantage]] class feature.

**Source:** `= this.source` (`= this.source-type`)
