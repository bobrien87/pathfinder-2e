---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Cursebound]]", "[[Divine]]", "[[Oracle]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Voices whisper to you how to best lay a creature low. You target one creature within 60 feet; if it has any weaknesses, you learn them, as well as which of its saving throw modifiers is lowest. You also come to understand its movements, gaining a +2 status bonus to your next attack roll (or skill check made as part of an attack action) against that foe before the end of your turn. The target is then temporarily immune for 1 day.

**Source:** `= this.source` (`= this.source-type`)
