---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Kitharodian Actor|Kitharodian Actor]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Emotion]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Kitharodian Actor Dedication"
frequency: "once per day"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** You are reduced to 0 Hit Points by a creature within 30 feet, but not immediately killed

You've watched dozens of morbid comedies depicting Beldam I, Taldor's prankster emperor whose wife accidentally killed him when she struck him with a marble bust after he jumped out from behind curtains to frighten her. You are reminded of this depressing yet perversely comical tale whenever you are near death, and in your final moments of consciousness you murmur a bleak joke to the creature who reduced you to 0 Hit Points. The creature must attempt a [[Will]] save against your class DC.
- **Critical Success** The target is unaffected.
- **Success** The target is distracted by giggles and can't use reactions until the beginning of your next turn.
- **Failure** The target laughs uncontrollably. It can't use reactions until the beginning of your next turn and is [[Slowed]] 1.
- **Critical Failure** As failure, but the target also immediately falls [[Prone]].

**Source:** `= this.source` (`= this.source-type`)
