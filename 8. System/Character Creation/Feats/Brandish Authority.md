---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Archfiend|Archfiend]]"
source-type: "Remaster"
level: "18"
traits: ["[[Auditory]]", "[[Mythic]]", "[[Visual]]"]
prerequisites: "Archfiend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a terrifying pronouncement, you manifest a visible sign of your authority and fiendish power, such as a crown of flame upon your brow, a scepter forged of solidified souls, or a throne comprised of a dozen dragon skulls. This object appears in your space or in your hand, as appropriate, and remains for 1 minute. When your sign of power appears, attempt an Intimidation check to [[Demoralize]] each enemy within 30 feet who can see or hear you. These Demoralize attempts don't take any penalty for not sharing a language. As long as your sign of power remains manifested, your enemies can't reduce the value of their [[Frightened]] condition below 1.

You can spend 1 Mythic Point as part of performing this action; if you do, frightened creatures grovel before you, in awe of your terrible power. At the beginning of their turn, a creature that has the frightened condition from Brandish Authority must attempt a [[Will]] save saving throw against your class DC or spell DC, whichever is higher. On failure, they must [[Drop Prone]]. On a critical failure, they must Drop Prone and can't Stand this turn.

**Source:** `= this.source` (`= this.source-type`)
