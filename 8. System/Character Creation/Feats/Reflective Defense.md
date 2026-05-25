---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Light]]", "[[Talos]]"]
frequency: "once per PT10M"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

**Trigger** A creature within 30 feet of you targets you, and you can see the attacker.

**Requirements** You are in dim or bright light.

Your body's natural luster has been polished to a gleaming shine. You use this to reflect light back into your enemy's eyes, disrupting its aim and focus; it must succeed at a Reflex save against your class DC or be [[Dazzled]] until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
