---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pactbinder|Pactbinder]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Occult]]"]
prerequisites: "Pactbinder Dedication, master in Occultism"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've studied pacts at Cobyslarni, or learned under someone who has, and understand them to not only create a bargain between individuals, but a separate entity altogether: the pact itself. You gain the [[Entreat Pact]] action, which you can use in association with any pact from the pactbinder archetype. For example, if you have the [[Pact of Draconic Fury]], you could Entreat Pact to aid a skill check to obtain an item the dragon desires.

**Special** Your pacts continually enforce themselves in a circular magical loop. You lose the ability to retrain out of any feats from the pactbinder archetype.

**Source:** `= this.source` (`= this.source-type`)
