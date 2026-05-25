---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Dandy|Dandy]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Fortune]]"]
prerequisites: "Dandy Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An ally within 30 feet fails a Will saving throw against a mental effect.

You expect the same level of urbane sophistication from your allies as you possess, so whenever one of them succumbs to egregious behavior from a mental effect, you're immediately mortified. How dare they make you look bad! Whether you respond with noisy contempt or quiet distress, your reaction gives your ally a second chance to shake off the effect and save the moment, at least socially. Your ally rerolls the triggering Will saving throw with a +1 circumstance bonus and uses the higher result. Regardless of the result of the save, your ally is temporarily immune to Such a Disgrace! for 10 minutes.

> [!danger] Effect: Such a Disgrace!

**Source:** `= this.source` (`= this.source-type`)
