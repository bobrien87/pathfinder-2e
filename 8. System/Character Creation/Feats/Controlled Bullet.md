---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beast Gunner|Beast Gunner]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Magical]]"]
prerequisites: "Beast Gunner Dedication"
frequency: "once per day"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You guide your weapon's next shot by taking control of the projectile directly, steering it through the air to hit target after target. Make a beast gun Strike against a creature within the first range increment. On a hit, the shot tears through the target and continues toward another target you can see. You make a Strike against this new target. The new target must be no farther from the previous target than a distance equal to the beast gun's range increment. For example, the new target must be within 150 feet of the previous target when attacking with a *drake rifle*. On a hit, you can direct the bullet toward a new target.

You can continue to make Strikes against new targets in this same way until your attack misses, at which point your shot dissipates. You can't make a Strike against a target you already attacked during this use of Controlled Bullet, but you can otherwise continue to make attacks against valid targets until you miss. Each attack counts toward your multiple attack penalty, but don't increase your penalty until you've made all your attacks.

**Source:** `= this.source` (`= this.source-type`)
