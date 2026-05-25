---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "trained in Occultism"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your talismans ward against foul magic. During your daily preparations, you can assemble a small pouch with bits of herbs, hair, sacred oils, and other ritual ingredients, which you give to one ally; the ally cannot be yourself. The first time that day the ally attempts a saving throw against a spell or haunt, they gain a +1 circumstance bonus to the roll. This bonus increases to +2 if you're an expert in Occultism or +3 if you're legendary.

> [!danger] Effect: Root Magic

**Source:** `= this.source` (`= this.source-type`)
