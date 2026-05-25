---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Concentrate]]", "[[Gunslinger]]"]
prerequisites: "way of the sniper"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a loaded firearm or crossbow.

You attempt to finish your target with a final, well-placed shot. Make a crossbow or firearm Strike. If you've damaged the target within the last minute with the same weapon and you get a critical success on your attack roll, the target must succeed at a [[Fortitude]] save against your class DC or die; this is a death and incapacitation effect. A creature that survives is temporarily immune for 1 day. Creatures with no head (such as dullahans or oozes) are immune to this ability, and creatures with redundant heads (such as ettins) might survive the destruction of a head.

**Source:** `= this.source` (`= this.source-type`)
