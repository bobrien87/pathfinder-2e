---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Cursebound]]", "[[Divine]]", "[[Healing]]", "[[Oracle]]", "[[Spirit]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You lay a finger on the scales of life and death to heal a creature, regardless of whether it's living or undead. You restore @Damage[(2*(1+@actor.level))[healing]] Hit Points to one creature within 30 feet.

In addition, you can mediate during your daily preparations to place yourself on one side of the scales. Choose life or death. If you align yourself with life, you can be targeted and healed by vitality healing effects, as normal for most living creatures; if you align yourself with death, you gain the void healing ability, and can instead be targeted and healed by void effects and other effects that restore Hit Points to undead creatures..

**Source:** `= this.source` (`= this.source-type`)
