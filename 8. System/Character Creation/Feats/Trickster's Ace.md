---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Concentrate]]", "[[Investigator]]", "[[Rogue]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You specify the trigger when you make your daily preparations (see Requirements below).

**Requirements** When you make your daily preparations, you must specify a trigger for this reaction using the same restrictions as the triggers for the Ready action. You also choose a single spell from the arcane, divine, occult, or primal list of 4th level or lower. The spell can't have a cost, nor can its casting time be more than 10 minutes. The spell must be able to target a single creature, and you must be a valid target for it.

Whether from jury-rigged magic items, deduction from the study of magical interactions, or other means, you have a contingency in your back pocket for desperate situations. When the trigger occurs, you cause the spell to come into effect. The spell targets only you, no matter how many creatures it would affect normally. If you define particularly complicated conditions, as determined by the GM, the trigger might fail. Once the contingency is triggered, the spell is expended until your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
