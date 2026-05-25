---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "7"
cast: "1 day"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You tap into other mortals' memories, knowledge, legends, tales, and lore about a subject. The subject must be an important person, place, or thing. If the subject is present, increase the degree of success of your primary skill check by one step. If you have only vague information about the subject before attempting the ritual, decrease the degree of success of your primary skill check by one step. These modifiers cancel each other out if you have a subject present with little to no baseline information.
- **Critical Success** For 1 hour after the ritual ends, you sort through memories that are mostly coherent, emphasizing more accurate or useful information over misremembered knowledge or exaggerated tales.
- **Success** For 1 hour after the ritual ends, you learn useful information for further inquiry that remains generally incomplete or enigmatic. As is the nature of mortal memory and stories, you are likely to learn multiple contradictory versions.
- **Failure** You fail to learn any useful legends.
- **Critical Failure** Your mind becomes overwhelmed with the vast array of knowledge at your disposal. You can't sense or respond to anything in the present for 1 week except to perform necessities like breathing and sleeping. When you recover, however, you can retrain one of your skills into a Lore based on the knowledge of a subject you were accessing, as if you had spent 1 week retraining.

**Source:** `= this.source` (`= this.source-type`)
