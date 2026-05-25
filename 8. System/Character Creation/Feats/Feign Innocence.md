---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Twilight Talon|Twilight Talon]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Twilight Talon Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You convince a creature that, despite appearances, you're on its side. Choose an enemy within 60 feet, and attempt a [[Deception]] check against its Will DC. The target is then temporarily immune to Feign Innocence for 1 hour. If you've taken a hostile action against it this round, your result can be no better than a failure.
- **Critical Success** You and the target are considered allies until the end of your next turn or until you take a hostile action against it, whichever comes first. In order to take a hostile action against you, the target must succeed at a Will save against your Deception DC or it loses the action.
- **Success** As critical success, but lasts until the end of your turn or until you take a hostile action against it, whichever comes first.
- **Failure** No effect.
- **Critical Failure** The target knows you attempted to fool it and plays along. You're [[Off Guard]] to the target until the beginning of your next turn.

**Source:** `= this.source` (`= this.source-type`)
