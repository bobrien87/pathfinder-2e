---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "4"
cast: "4 hours"
source: "Pathfinder #201: Pactbreaker"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You tap into Corazal's innumerable senses to identify disturbances throughout the Verduran Forest.
- **Critical Success** You and Corazal successfully identify a flashpoint: an imminent event that could stoke distrust and unrest. You experience a sensory premonition of the event, can cast know the way as a 7th-rank cantrip to point toward the location, and know which Elder Oak is closest to it.
- **Success** As success, but the ritual heavily taxes your mind and body. You are [[Drained]] 1, and until the drained condition ends, you are also [[Stupefied 1]].
- **Failure** The ritual has no effect.
- **Critical Failure** The ritual has no effect beyond burning your mind with conflicting information. You are [[Drained]] 2, and until the drained condition ends, you are also stupefied 1 and have the Dubious Knowledge skill feat. Whenever you would decrease this drained value, the value does not decrease unless you succeed at a DC 11 flat check.

**Source:** `= this.source` (`= this.source-type`)
