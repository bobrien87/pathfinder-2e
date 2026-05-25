---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Elf]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You work at a pace born from longevity that enhances your thoroughness. You can voluntarily spend twice as much time as normal on a Perception check or skill check that takes 1 action or longer. If you do, you gain a +2 circumstance bonus to the check and don't automatically reduce your degree of success on a natural 1 (you get a critical failure only if your result is 10 lower than the DC). For example, you could get these benefits if you spent 2 actions to [[Seek]], which normally takes 1 action. You can get these benefits during exploration by taking twice as long exploring as normal, or in downtime by spending twice as much downtime.

The GM might determine a situation doesn't grant you a benefit if a delay would be directly counterproductive to your success, such as a tense negotiation with an impatient creature.

**Source:** `= this.source` (`= this.source-type`)
