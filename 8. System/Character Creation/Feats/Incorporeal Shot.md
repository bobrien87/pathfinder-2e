---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eldritch Archer|Eldritch Archer]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Magical]]"]
prerequisites: "Eldritch Archer Dedication"
frequency: "once per day"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You can concentrate an immense amount of magic to create a piece of ammunition that phases through everything but your target.

Make a bow or crossbow Strike against a foe who is [[Observed]] or [[Hidden]] to you (but not [[Undetected]]).

The ammunition travels to your target in a straight line, passing through any non-magical barriers or walls in its way, though magical barriers stop the arrow. The shot ignores all cover, the [[Concealed]] condition, the hidden condition, and circumstance bonuses to AC from shields. It has a +4 status bonus to hit creatures wearing any type of armor.

The Strike's damage can't be reduced with a Shield Block reaction using a non-magical shield.

**Source:** `= this.source` (`= this.source-type`)
