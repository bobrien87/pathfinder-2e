---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wild Mimic|Wild Mimic]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Wild Mimic Dedication, you have seen a creature use Trample or have identified a creature with Trample in combat"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You Stride up to double your speed and can move through the spaces of creatures at least one size smaller, trampling each creature whose space you enter. You can attempt to trample the same creature only once in a single use of Trample Mimicry. You deal @Damage[(ternary(gte(@actor.level,18),5,ternary(gte(@actor.level,14),4,3)))d12[bludgeoning]|options:area-damage] damage to each trampled creature ([[Reflex]] save against the higher of your class DC or spell DC). This damage increases by 1d12 at levels 14 and 18.

**Source:** `= this.source` (`= this.source-type`)
