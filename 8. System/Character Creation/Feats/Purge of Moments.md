---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Time Mage|Time Mage]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Concentrate]]"]
prerequisites: "Time Mage Dedication"
frequency: "once per PT1H"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

All things eventually end, a truth that you can put into practice by accelerating your passage through time to shake off harmful effects. Five rounds of apparent time occur for you. No one, including you, can act during this time, but effects on you run their course, including beneficial effects, negative effects, afflictions, conditions, and persistent damage. Roll saving throws, flat checks, damage, and any other rolls for those effects normally as if the time had passed. Excessive use of this technique is responsible for more than a few premature gray hairs among time mages.

**Source:** `= this.source` (`= this.source-type`)
