---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ghost|Ghost]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Divine]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]"]
prerequisites: "Headless Haunt"
frequency: "once per day"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You shriek a death sentence upon a single target within 120 feet, forcing it to experience the final moments of your mortal life as you were dragged through a howling mob and forced to kneel before the final blade that took your life and head. The target is subject to the effects of a 5th-rank [[Vision of Death]] with a DC equal to your class DC or spell DC, whichever is higher. If you slay a significant foe with this ability, its physical body is gruesomely decapitated, forcing its allies within 15 feet to attempt a Will save against the same DC or be [[Frightened]] 1 ([[Frightened]] 2 on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
