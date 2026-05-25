---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wrestler|Wrestler]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Wrestler Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your grasp has a supernatural quality to it, preventing your foes from easily escaping—with or without magical assistance. If a creature you have [[Grabbed]] attempts to use a teleportation spell or effect, it must succeed at a DC 15 flat check or the spell fails. If a creature you have grabbed attempts to [[Escape]] while under the effect of [[Unfettered Movement]] or a similar effect, it must succeed at a DC 15 flat check or be forced to roll the Escape attempt normally, rather than automatically succeeding.

> [!danger] Effect: Inescapable Grasp

**Source:** `= this.source` (`= this.source-type`)
