---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Viking|Viking]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Viking Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a one-handed melee weapon in one hand and a shield in another hand.

You charge into battle with shield-splintering fury. You [[Leap]], Stride, or Swim. Make two melee Strikes during this movement, one with your one-handed melee weapon and one with your shield or a weapon attached to the shield (like a shield boss or shield spikes). You can make these Strikes at any points during your movement, and each must target a different enemy. Both attacks count toward your multiple attack penalty, but don't increase your penalty until you have made both attacks.

**Source:** `= this.source` (`= this.source-type`)
