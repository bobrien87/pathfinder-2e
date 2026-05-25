---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Shared Archetype Feats|Shared Archetype Feats]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]"]
prerequisites: "Acrobat or Gladiator Dedication, legendary in Acrobatics"
frequency: "once per PT1H"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You Delay.

**Frequency** once per hour

You are always ready to embrace to a change in tempo and adapt your actions to take advantage of unforeseen developments. When you return to the initiative order after you Delay, you do so in an unpredictable way. All enemies are [[Off Guard]] to you until the start of your next turn, and you become [[Quickened]] for the current round but can only use the extra action to Stride or Strike.

**Source:** `= this.source` (`= this.source-type`)
