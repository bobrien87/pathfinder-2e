---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eternal Legend|Eternal Legend]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]"]
prerequisites: "Eternal Legend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are adjacent to a climbable surface at least 10 feet tall.

Seemingly to defy gravity, you use a nearby vertical surface to propel yourself upward and then strike downward like the driving rain. Stride up to half your Speed upward on the required surface; if you have a climb Speed, you may use your full climb Speed instead. The surface does not need to span the full height of your Stride. You can then either make a ranged Strike at a target within your weapon's first range increment and land in the space you began (or an adjacent space) without taking falling damage, or you can land in a space adjacent to a creature within 10 feet of the required surface without taking falling damage and make a melee Strike against that creature. Either Strike deals an extra two dice of weapon damage. In addition, the target dealt damage by your Strike must succeed at a [[Fortitude]] save saving throw against your class DC or become [[Stunned]] 1.

**Source:** `= this.source` (`= this.source-type`)
