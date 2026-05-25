---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Overwatch|Overwatch]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]"]
prerequisites: "Overwatch Dedication, master in Perception"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You make a successful ranged attack against an opponent who is within your overwatch field, and who is within reach of one or more of your allies who is also within your overwatch field.

Informing your ally of an opening created by your shot, you coordinate to set them up to hit the target at the same time. Your ally can make a melee Strike against the triggering foe as a reaction. This Strike doesn't count toward that ally's multiple attack penalty, and their multiple attack penalty doesn't apply to this Strike. If your ally's Strike is successful, combine the damage from your successful ranged attack with the damage from your ally's melee attack for the purpose of determining resistances and weaknesses.

**Source:** `= this.source` (`= this.source-type`)
