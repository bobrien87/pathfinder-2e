---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Medic|Medic]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Healing]]", "[[Manipulate]]", "[[Skill]]"]
prerequisites: "Medic Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are holding healer's tools, or you are wearing them and have a hand free.

You treat an adjacent creature in an attempt to reduce the clumsy, enfeebled, or sickened condition. If a creature has multiple conditions from this list, choose one. Attempt a counteract check against the condition using your Medicine modifier as your counteract modifier and the condition's source to determine the DC. You can't treat a condition that came from an artifact or effect above 20th level unless you have Legendary Medic; even if you do, the counteract DC increases by 10. Treating a Condition that is continually applied under certain circumstances (for instance, the enfeebled condition a holy character gains from carrying a weapon with the unholy rune) has no effect as long as the circumstances continue.
- **Critical Success** Reduce the condition value by 2.
- **Success** Reduce the condition value by 1.
- **Critical Failure** Increase the condition value by 1.

**Source:** `= this.source` (`= this.source-type`)
