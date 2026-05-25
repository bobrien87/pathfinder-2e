---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Automaton]]"]
frequency: "once per day"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** You have the [[Dying]] condition and are about to attempt a recovery check.

Your soul taps into your core's power to push against the grasp of death and allow you to recover consciousness. You're restored to 1 Hit Point, lose the dying and [[Unconscious]] conditions, and can act normally on this turn. You gain or increase the wounded condition as normal when losing the dying condition in this way.

**Enhancement** Your soul can draw even more power from your core, granting you additional benefits. When you use Core Rejuvenation, you also gain a number of temporary Hit Points equal to three times your level. These Hit Points remain for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
