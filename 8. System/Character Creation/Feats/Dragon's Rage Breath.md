---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Barbarian]]", "[[Concentrate]]", "[[Rage]]"]
prerequisites: "dragon instinct"
frequency: "once per PT10M"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

You breathe deeply and exhale powerful energy in a @Template[cone|distance:30], dealing @Damage[(@actor.level)d6[@actor.flags.system.barbarian.instinct.dragon.damageType]|options:area-damage] damage to each creature in the area with a [[Reflex]] save against your class DC. The damage type matches your instinct's dragon breath, and this action gains the trait of your dragon instinct's tradition.

**Source:** `= this.source` (`= this.source-type`)
