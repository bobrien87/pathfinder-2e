---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Golden Legionnaire|Golden Legionnaire]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Golden Legionnaire Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Long hours of experimentation with the Platinum Wing have familiarized you with experimental weaponry. You have familiarity with martial firearms and alchemical bombs, treating them as simple weapons for the purposes of proficiency. You ignore the penalty for making ranged attacks within your second range increment with alchemical bombs. You gain access to uncommon firearms and alchemical bombs.

**Source:** `= this.source` (`= this.source-type`)
