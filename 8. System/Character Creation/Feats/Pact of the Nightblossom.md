---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pactbinder|Pactbinder]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Occult]]"]
prerequisites: "Pactbinder Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've sworn a pact with Jenway Nightblossom of the Synod of Truth in Dreams, a talented oneiromancer and pactbinder. Through your connection to her, you're able to divine your dreams for wisdom, and they're protected from interference. You're immune to [[Nightmare]]. During your daily preparations, if you slept and were able to dream, you learn a helpful piece of advice about your future activities, as [[Read Omens]].

As payment, Jenway established a permanent telepathic connection to you that functions whenever you sleep or dream. Whenever you learn something significant, Jenway learns it the next time you sleep. You can withhold information, but you lose the benefits of Pact of the Nightblossom until you relent and allow Jenway to learn it.

**Source:** `= this.source` (`= this.source-type`)
