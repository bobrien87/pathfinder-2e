---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Field Propagandist|Field Propagandist]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Field Propagandist Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you seek to convince others of the worth of your cause, you are capable of unleashing such an entrancing torrent of rhetoric and metaphor that it is all but impossible to look away from you. When you begin a conversation or similar attempt with the goal of Making an Impression, all creatures who are observing you become [[Fascinated]] unless they succeed at a [[Will]] save against the higher of your class DC or spell DC. Creatures who are familiar with you and your verbal techniques, such as allies you've known for at least several days, are immune to this effect, though newer allies who have not heard one of your speeches before might still be affected.

Affected creatures remain fascinated for as long as you continue your filibuster, though they can attempt a new save to end the effect at the end of each minute while your filibuster lasts. A creature who succeeds at a saving throw to end the fascinated condition from your filibuster is also unaffected by your attempt to [[Make an Impression]].

You can continue your filibuster indefinitely, but after every 10 minutes you must attempt a [[Fortitude]] save saving throw against a hard DC for your level. Failing this save results in your filibuster ending and prevents you from attempting another filibuster for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
