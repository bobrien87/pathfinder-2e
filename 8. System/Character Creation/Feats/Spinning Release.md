---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Thlipit Contestant|Thlipit Contestant]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Mental]]"]
prerequisites: "Thlipit Contestant Dedication"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a creature [[Grabbed]] or [[Restrained]] with your lash.

You wind your lash around your opponent, then spin them rapidly to discombobulate them. You release your opponent, sending them wobbling 10 feet in a direction of your choice; this is forced movement. Your opponent must succeed at a [[Fortitude]] save against your class DC, with the following effects.
- **Failure** The target is [[Confused]] until the end of their next turn. They are then temporarily immune to being confused or sickened by Spinning Release for 10 minutes, though the ability can still be used to move them.
- **Critical Failure** As failure, but the target is also [[Sickened]] 1 from being spun around.

**Source:** `= this.source` (`= this.source-type`)
