---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Air]]", "[[Auditory]]", "[[Illusion]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Speaking lies, you set them loose upon a drifting wind. You create an auditory illusion that comes from a square within 500 feet and can be as loud as four normal humans talking. The sound can be intricate, including speech or music, though the GM might require you to attempt a check or know a language for it to be convincing. The illusion lasts until the end of your next turn, and you can Sustain the impulse.

You can have any creature within 40 feet of the illusion, or that comes within 40 feet of it during the duration, attempt a [[Will]] save against your class DC. This is a mental effect.
- **Success** The creature is unaffected, disbelieves the illusion, and is temporarily immune for 1 hour.
- **Failure** The creature is [[Fascinated]] with the source of the sound until the end of its next turn. When the fascination ends, the creature is temporarily immune for 1 hour.
- **Critical Failure** As failure, but the creature is fascinated for 1 minute or until it disbelieves.

**Source:** `= this.source` (`= this.source-type`)
