---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sleepwalker|Sleepwalker]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]"]
prerequisites: "Sleepwalker Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You draw no distinction between the sleeping and waking worlds. Your [[Daydream Trance]] has an unlimited duration, and you no longer need to take an action to enter it. If you're [[Unconscious]] due to sleep, you don't take the –4 penalty to AC, Perception, and Reflex saves, and don't have the [[Off Guard]] condition. You're still [[Blinded]] while asleep. You can act on your turn while asleep, though you're [[Slowed]] 2 until you fully awaken.

**Source:** `= this.source` (`= this.source-type`)
