---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Cavalier|Cavalier]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Cavalier Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are riding a mount that has a melee Strike using its legs (claw, talons, hoof, etc.).

You urge your mount to charge into the fray, trampling all enemies who stand in your path. You command your mount to Stride up to double its Speed (or to [[Burrow]], [[Climb]], [[Fly]], or [[Swim]], if it has the corresponding movement type), moving through the spaces of any foes in your path up to one size smaller than your mount. Your mount deals the damage of one of its melee Strikes to each creature whose space you move through, with a basic Reflex save against your mount's Athletics DC. On a critical failure, the creature also becomes [[Off Guard]] until the end of your next turn. Roll the damage only once. You can damage a given creature only once during this movement.

**Source:** `= this.source` (`= this.source-type`)
