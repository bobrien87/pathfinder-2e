---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Timewracked|Timewracked]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]", "[[Occult]]"]
prerequisites: "Timewracked Dedication"
frequency: "once per day"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** Your turn ends.

Sometimes, your actions are so successful and impressive that it's worth going back to them. Note the actions you took during the turn that just ended (excepting the reaction you used to trigger Preserve the Moment), including the die roll results (not the actual check results). Die rolls you made as a result of others' actions on you or from the environment are not recorded. For example, if you Stride up to a firewyrm, roll a basic Reflex save against its intense heat aura, then Strike the firewyrm with a longsword, and then Climb up an adjacent wall, when you activate Preserve the Moment you record only the Stride action, the Strike action (and the die roll result you roll for the Strike), and the Climb action (and the die roll result you roll for the Athletics check to do so); you do not record your Reflex save against the aura's effects. Preserve the Moment works best, as a result, when the actions you take are relatively standard and when rolls associated with those are high rolls.

You gain the [[Restore the Moment]] reaction, which you can use once during the next 24 hours.

**Source:** `= this.source` (`= this.source-type`)
