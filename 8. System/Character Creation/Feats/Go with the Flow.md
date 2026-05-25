---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[General]]", "[[Secret]]", "[[Skill]]"]
prerequisites: "master in Occultism"
frequency: "once per day"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** A creature detects your attempt to [[Impersonate]], and you're within 30 feet of at least one other creature.

You have an occult connection to the world that helps you blend in with the cacophony of life around you. Attempt an [[Occultism]] check against the creature's Perception DC. On a success, the creature mistakenly identifies another creature within 30 feet of you as you instead.

**Source:** `= this.source` (`= this.source-type`)
