---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Bullet Dancer|Bullet Dancer]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]"]
prerequisites: "Bullet Dancer Dedication, Trick Shot"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a simple firearm or simple combination weapon.

When using a simple firearm, you can shoot objects right out of your enemy's hands. Attempt to [[Disarm]] the target using a ranged attack roll with the required firearm or combination weapon, instead of attempting an Athletics check against the target's Reflex DC.

**Source:** `= this.source` (`= this.source-type`)
