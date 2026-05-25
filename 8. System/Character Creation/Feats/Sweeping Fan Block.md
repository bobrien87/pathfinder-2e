---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Fan Dancer|Fan Dancer]]"
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Archetype]]"]
prerequisites: "Fan Dancer Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You're targeted by a ranged attack that uses ammunition.

**Requirements** You're wielding two fans, one in each hand.

You leap up on one leg, snapping your fans open alongside your head before sweeping them across your body. When you're the target of an attack using ammunition (such as arrows, bolts, sling bullets, and other objects of similar size) while wielding two fans, whirl your fans to disrupt the incoming attack with gusts of air, gaining a +2 circumstance bonus to AC against the triggering attack. If the triggering attack misses, you can redirect the ammunition into a nearby pocket or container where it can be retrieved and reused.

**Source:** `= this.source` (`= this.source-type`)
