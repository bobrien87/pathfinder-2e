---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pactbinder|Pactbinder]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Primal]]"]
prerequisites: "Pactbinder Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've sworn a pact with Ng the Hooded, the Eldest known as the Lord of the Crossroads, though your only sign of Ng's acknowledgment is the benefits you receive. Anyone tracking you must succeed at a [[Survival]] check against the higher of your class DC and spell DC. Creatures attempting to remember your features after the first time meeting you must succeed at a [[Will]] save against the same DC. If they fail, they recall the meeting but none of your features.

In exchange, you must continue your wanderings, never settling in one place for longer than one month, or you lose the benefits of this feat until you begin your travels again. If you ever willingly tell anyone you've formed a pact with Ng, you lose the benefits of this feat permanently, though you can share vague information about the pact's effects.

**Source:** `= this.source` (`= this.source-type`)
