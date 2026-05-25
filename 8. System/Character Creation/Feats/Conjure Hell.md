---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellknight|Hellknight]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Divine]]", "[[Fire]]", "[[Manipulate]]", "[[Spirit]]", "[[Unholy]]"]
prerequisites: "Hellknight Signifer Preferment"
frequency: "once per day"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Though you might not worship Asmodeus or other devils, you've studied enough of Hell to call forth a brief burst of its fire. Each creature in a @Template[type:burst|distance:15] within 120 feet takes @Damage[(2*floor(@actor.level/2) - 3)d6[fire]|options:area-damage] damage with a [[Fortitude]] save against your spell DC. This fire damage ignores an amount of fire resistance equal to your level, but not immunity to fire. A creature that fails its save also has its soul set aflame, taking @Damage[2d6[persistent,spirit]|options:area-damage] damage (or @Damage[4d6[persistent,spirit]|options:area-damage] damage on a critical failure). At 14th level and every 2 levels thereafter, the initial fire damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
