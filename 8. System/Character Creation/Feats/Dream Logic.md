---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sleepwalker|Sleepwalker]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Mental]]", "[[Occult]]"]
prerequisites: "Sleepwalker Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can transmit a sense of dreamy nonchalance. If you do something especially strange or dangerous while you're in your Daydream Trance, such as entering a restricted area or fighting someone in the street, any creature that isn't one of your allies must attempt a [[Perception]] check against your class or spell DC, whichever is higher. On a success, it realizes something is amiss, and on a failure, it believes nothing is out of the ordinary. The creature can attempt a new check if you start doing something else strange, but not if you continue on the same course of action it already failed to notice was peculiar.

Any hostile action by you or your allies against an affected creature automatically ends the effect for that creature. The GM might allow the creature a new check if someone else brings your actions to its attention, such as if someone you're attacking calls out for help. When your trance ends, affected creatures retain their memories of events but likely still view them as unremarkable; unless they're prompted to relate the events, they might not report them.

**Source:** `= this.source` (`= this.source-type`)
