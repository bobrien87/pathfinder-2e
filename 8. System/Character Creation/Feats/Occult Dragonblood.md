---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Dragonblood]]", "[[Lineage]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your blood contains a tiny fragment of unusual or inexplicable power from a mysterious dragon, such as a conspirator dragon or omen dragon. You are drawn to the stranger parts of the world and can generally spot them with a glance. You gain the trained proficiency rank in Occultism. If you would automatically become trained in Occultism (from your background or class, for example), you instead become trained in a skill of your choice. You gain the [[Oddity Identification]] skill feat. If you choose a draconic exemplar, you must choose an occult dragon.

**Source:** `= this.source` (`= this.source-type`)
