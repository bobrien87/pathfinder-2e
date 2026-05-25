---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eternal Legend|Eternal Legend]]"
source-type: "Remaster"
level: "14"
traits: ["[[Flourish]]", "[[Mythic]]"]
prerequisites: "Eternal Legend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You make a forceful attack that has the power to push your foe through walls. Spend a Mythic Point and make a Strike at mythic proficiency. If you hit and deal damage to the target, you push them up to 15 feet away from you. If this movement would cause the target to collide with an object that has a hardness of 5 or less, the object breaks and the target is pushed through the object's space for the remainder of the forced movement, taking an additional 2d6 bludgeoning damage (the GM can decide that this is a different type of damage depending on the object the target was pushed through; for instance, slashing damage if the target is pushed through a pane of glass).

If the forced movement doesn't cause the target to collide with an object, the target must succeed at a [[Reflex]] save saving throw against your class DC or be knocked [[Prone]] at the end of the movement.

**Source:** `= this.source` (`= this.source-type`)
