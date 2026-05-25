---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ritualist|Ritualist]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "expert in Arcana, Nature, Occultism, or Religion"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have begun to master the difficult art of casting rituals. You gain a +2 circumstance bonus to all checks to perform a ritual. You learn two uncommon rituals of 2nd rank or lower. You must meet all prerequisites to be the primary caster of a ritual to select it, and you can't teach it to anyone else or allow someone else to serve as primary caster unless they know the ritual as well.

At 8th level and every 4 levels thereafter, you learn two more rituals with the same restrictions and with a maximum rank of half that level.

Ritualist

**Source:** `= this.source` (`= this.source-type`)
