---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Psychic Duelist|Psychic Duelist]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Illusion]]", "[[Incapacitation]]", "[[Mental]]", "[[Occult]]"]
prerequisites: "Psychic Duelist Dedication"
frequency: "once per day"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You attempt to enter a psychic duel with a creature within 100 feet. The target can attempt a [[Will]] save against the higher of your spell DC or class DC. If it enters the duel willingly, use the result for a critical failure.
- **Critical Success** The target is unaffected.
- **Success** The two of you enter a psychic duel, but it ends automatically at the end of your next turn. As normal for a psychic duel, the duel ends if one participant is knocked out, as well as under any other conditions to which both participants agree. If you're in initiative when you Instigate the Psychic Duel, you keep the same initiative positions. You can each choose a psychic center for any skill in which you're trained, as you would if you were using that skill to roll initiative for the duel.
- **Failure** As a success, except instead of ending at the end of your next turn, the target can attempt a new save to end the duel at the end of each of your turns, starting with your next turn.
- **Critical Failure** As a success, except the duel doesn't end until it reaches one of the normal end conditions for a psychic duel.

**Source:** `= this.source` (`= this.source-type`)
