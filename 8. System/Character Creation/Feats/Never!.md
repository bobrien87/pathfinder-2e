---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Guardian]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The idea that you would hurt your companions, even when you've lost your reason, is unthinkable. Each time you would attack an ally due to being [[Confused]] or controlled, you can attempt another saving throw against the effect that caused you to be confused or controlled with a +4 circumstance bonus to the save. If you succeed, you don't make the attack, though you still expend any actions it would have taken. If your save ends the effect making you confused or controlled, you can take any remaining actions during your turn as normal. Failing or critically failing this additional save doesn't increase the effect's duration or otherwise worsen it.

**Source:** `= this.source` (`= this.source-type`)
