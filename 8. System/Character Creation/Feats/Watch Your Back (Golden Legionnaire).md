---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Golden Legionnaire|Golden Legionnaire]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Golden Legionnaire Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You shout a warning to an ally about encroaching foes. Choose a target ally within 60 feet. Until the beginning of your next turn, the target can't be [[Off Guard]] due to flanking.

> [!danger] Effect: Watch Your Back (Golden Legionnaire)

**Source:** `= this.source` (`= this.source-type`)
