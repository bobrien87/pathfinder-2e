---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Rivethun Invoker|Rivethun Invoker]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Healing]]"]
prerequisites: "Rivethun Invoker Dedication"
frequency: "once per day"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** You fail or critically fail a saving throw against a curse, death, emotion, or fear effect.

You leverage your emotional turmoil to mend your physical form. You regain @Damage[(2*(max(1,(@actor.system.skills.athletics.rank - 1))))d8[healing]] Hit Points. If you're a master in Athletics, you regain 4d8 Hit Points instead. If you're legendary in Athletics, you regain 6d8 Hit Points instead.

**Source:** `= this.source` (`= this.source-type`)
